import numpy as np
from utils.constants import EARTH_MU, EARTH_RADIUS
from environment.gravity import J2_zonal_harmonics
from typing import List


class OrbitModel:
    def __init__(self):
        self.mu = EARTH_MU
        self.r_earth = EARTH_RADIUS

    def two_body_ode(self,
                     position: List | np.ndarray,
                     velocity: List | np.ndarray
                     ):

        if np.shape(position) != (3,):
            raise ValueError('Position must be of shape (3,)')
        if np.shape(velocity) != (3,):
            raise ValueError('Velocity must be of shape (3,)')

        # implement perturbations

        # J2 zonal harmonics
        acceleration_gravity = J2_zonal_harmonics(position,
                                                  EARTH_MU, EARTH_RADIUS)

        # calculate unperturbed acceleration from two body equations
        acceleration_unperturbed = (-(self.mu / np.linalg.norm(position)**3)
                                    * position)

        # perturbed acceleration
        acceleration = acceleration_unperturbed + acceleration_gravity

        return np.array([
            velocity[0], velocity[1], velocity[2],
            acceleration[0], acceleration[1], acceleration[2]
        ])
