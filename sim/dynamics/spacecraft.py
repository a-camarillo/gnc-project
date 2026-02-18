from sim.dynamics.attitude import AttitudeModel
from sim.dynamics.orbit import OrbitModel
from sim.environment.gravity import GravityField
from sim.math.quaternion import Quaternion
from sim.frames.conversions import lvlh2inertial
from numpy import concatenate, shape


class SpaceCraftModel:
    def __init__(self,
                 attitude_model: AttitudeModel,
                 orbit_model: OrbitModel
                 ):
        self.attitude = attitude_model
        self.orbit = orbit_model
        self.gravity = GravityField()

    def propagate(self, time, states):
        position = states[0:3]
        velocity = states[3:6]
        quaternion = states[6:10]
        angular_rate = states[10:]

        quaternion_repr = Quaternion(quaternion)

        # calculate orbital perturbations (to be modified in the future)
        gravity_perturbation = self.gravity.zonal_harmonics(position)

        # calculate disturbance torques (to be modified in the future)
        attitude_intertial2body = quaternion_repr.quaternion2rotation_matrix()
        matrix_lvlh2inertial = lvlh2inertial(position, velocity)
        attitude_lvlh2body = matrix_lvlh2inertial @ attitude_intertial2body
        gravity_gradient = self.gravity.gravity_gradient(
                position, self.attitude.inertia, attitude_lvlh2body)
        # calculate next states
        next_orbit_states = self.orbit.two_body_ode(position,
                                                    velocity,
                                                    gravity_perturbation)
        next_attitude_states = self.attitude.attitude_dynamics_kinematics(
                quaternion, angular_rate, external_torque=gravity_gradient)

        propagated_states = concatenate((next_orbit_states,
                                        next_attitude_states))
        return propagated_states
