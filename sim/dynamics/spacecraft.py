from sim.dynamics.attitude import AttitudeModel
from sim.dynamics.orbit import OrbitModel
from sim.environment.gravity import GravityField
from sim.environment.magnetic import MagneticField
from sim.math.quaternion import Quaternion
from sim.math.matrices import cross_product_matrix
from sim.frames.conversions import lvlh2inertial
from numpy import array, concatenate


class SpaceCraftModel:
    def __init__(self,
                 attitude_model: AttitudeModel,
                 orbit_model: OrbitModel,
                 environments: list[GravityField | MagneticField],
                 ):
        self.attitude = attitude_model
        self.orbit = orbit_model
        for environment in environments:
            if isinstance(environment, GravityField):
                self.gravity = environment
            elif isinstance(environment, MagneticField):
                self.magnetic = environment
            else:
                self.gravity = None
                self.magnetic = None
                self.atmosphere = None

    def propagate(self, time, states):
        position = states[0:3]
        velocity = states[3:6]
        quaternion = states[6:10]
        angular_rate = states[10:]

        quaternion_repr = Quaternion(quaternion)

        orbital_perturbations = array([0., 0., 0.])
        disturbance_torques = array([0., 0., 0.])

        # calculate disturbance torques (to be modified in the future)
        attitude_intertial2body = quaternion_repr.quaternion2rotation_matrix()
        matrix_lvlh2inertial = lvlh2inertial(position, velocity)
        attitude_lvlh2body = matrix_lvlh2inertial @ attitude_intertial2body

        # calculate gravitational effects
        if self.gravity:
            # orbit
            gravity_perturbation = self.gravity.zonal_harmonics(position)
            orbital_perturbations += gravity_perturbation

            # attitude
            gravity_gradient = self.gravity.gravity_gradient(
                    position, self.attitude.inertia, attitude_lvlh2body)
            disturbance_torques += gravity_gradient

        # calculate magnetic field effects
        if self.magnetic:
            # attitude only, magnetic field does not effect orbit
            magnetic_dipole = array([5., 5., 5.])  # Am^2
            mag_body = self.magnetic.mag_body
            magnetic_torque = (cross_product_matrix(magnetic_dipole) @
                               mag_body).reshape((-1,))
            disturbance_torques += magnetic_torque

        # calculate next states
        next_orbit_states = self.orbit.two_body_ode(position,
                                                    velocity,
                                                    orbital_perturbations)
        next_attitude_states = self.attitude.attitude_dynamics_kinematics(
                quaternion, angular_rate, external_torque=disturbance_torques)

        propagated_states = concatenate((next_orbit_states,
                                        next_attitude_states))
        return propagated_states
