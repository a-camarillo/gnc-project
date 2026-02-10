import numpy as np
from numpy.linalg import norm
from sim.utils.constants import EARTH_MU, EARTH_RADIUS


class Environment:
    def __init__(self):
        # gravitational parameter
        self.mu = EARTH_MU
        # radius of Earth in m
        self.r_earth = EARTH_RADIUS


class Gravity(Environment):
    def __init__(self):
        self.J2 = 0.00108263

    def zonal_harmonics(self, sc_r_I):
        x = sc_r_I[0]
        y = sc_r_I[1]
        z = sc_r_I[2]
        r = norm(sc_r_I)

        del_x = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((1 - 5*(z/r)**2)*(x/r)))
        del_y = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((1 - 5*(z/r)**2)*(y/r)))
        del_z = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((3 - 5*(z/r)**2)*(z/r)))

        return np.array([del_x, del_y, del_z])

    def gravity_gradient(self, sc_r_I, sc_J, attitude_B_LVLH):
        """
        Gravity gradient vector
        (3*mu/(r^3))*n x J*n
        where n is a nadir pointing unit vector in the body frame

        To find n we can use the fact that the nadir vector in the lvlh frame
        is [0 0 1]'

        Now all we need is the attitude of the body relative to the lvlh frame
        to get n_body = A_body_lvlh*n_lvlh
        """
        nadir = np.array([
            [0],
            [0],
            [1],
        ])

        n = attitude_B_LVLH @ nadir

        n_cross = np.array([
            [0, -n[2], n[1]],
            [n[2], 0, -n[0]],
            [-n[1], n[0], 0],
        ])
        return (3*self.mu/(sc_r_I**3))*(n_cross@(sc_J@n))
