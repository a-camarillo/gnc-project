import numpy as np
from typing import List
from math.matrices import cross_product_matrix


class AttitudeModel:
    def __init__(self,
                 sc_inertia: np.ndarray,
                 ):
        self.inertia = sc_inertia
        if np.shape(self.inertia) != (3, 3):
            raise ValueError('Inertia must be a matrix of shape (3, 3)')

    def attitude_dynamics_kinematics(self,
                                     quaternion: List | np.ndarray,
                                     angular_rate: List | np.ndarray,
                                     external_torque=np.array([[0], [0], [0]]),
                                     wheel_momentum=np.array([[0], [0], [0]]),
                                     ):
        if np.shape(angular_rate) != (3,):
            raise ValueError('Angular Rate must be of shape (3,)')
        if np.shape(quaternion) != (4,):
            raise ValueError('Quaternion must be of shape (4,)')

        angular_rate_x = cross_product_matrix(angular_rate)
        
        Omega = np.array([
                [0,  angular_rate[2], -angular_rate[1], angular_rate[0]],
                [-angular_rate[2], 0, angular_rate[0], angular_rate[1]],
                [angular_rate[1], -angular_rate[0], 0, angular_rate[2]],
                [-angular_rate[0], -angular_rate[1], -angular_rate[2], 0],
        ])

        # DYNAMICS
        angular_rate = angular_rate.reshape(-1, 1)
        angular_acceleration = (np.linalg.inv(self.inertia) @
                                (external_torque - angular_rate_x @
                                (self.inertia @ angular_rate + wheel_momentum))
                                )
        # KINEMATICS
        quaternion = quaternion.reshape(-1, 1)
        quaternion_dot = 0.5*Omega@quaternion

        attitude_states_dot = np.concatenate(
                (quaternion_dot, angular_acceleration))
        return attitude_states_dot.ravel()
