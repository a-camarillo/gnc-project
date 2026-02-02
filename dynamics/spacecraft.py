from dynamics.attitude import AttitudeModel
from dynamics.orbit import OrbitModel
from numpy import concatenate


class SpaceCraftModel:
    def __init__(self,
                 attitude_model: AttitudeModel,
                 orbit_model: OrbitModel
                 ):
        self.attitude = attitude_model
        self.orbit = orbit_model

    def propagate(self, time, states):
        position = states[0:3]
        velocity = states[3:6]
        quaternion = states[6:10]
        angular_rate = states[10:]

        next_orbit_states = self.orbit.two_body_ode(position, velocity)
        next_attitude_states = self.attitude.attitude_dynamics_kinematics(
                quaternion, angular_rate)

        propagated_states = concatenate(next_orbit_states,
                                        next_attitude_states)
        return propagated_states
