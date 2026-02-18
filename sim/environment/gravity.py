import numpy as np
from numpy.linalg import norm
from sim.environment.environment import Environment
from sim.math.matrices import cross_product_matrix


class GravityField(Environment):
    def __init__(self):
        super().__init__()
        self.J2 = 0.00108263

    def zonal_harmonics(self, position):
        x = position[0]
        y = position[1]
        z = position[2]
        r = norm(position)

        del_x = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((1 - 5*(z/r)**2)*(x/r)))
        del_y = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((1 - 5*(z/r)**2)*(y/r)))
        del_z = (-(3/2)*self.J2*(self.mu/r**2)*((self.r_earth/r)**2) *
                 ((3 - 5*(z/r)**2)*(z/r)))

        return np.array([del_x, del_y, del_z])

    def gravity_gradient(self, position, sc_inertia, attitude_B_LVLH):
        """
        Gravity gradient vector
        (3*mu/(r^3))*n x J*n
        where n is a nadir pointing unit vector in the body frame

        To find n we can use the fact that the nadir vector in the lvlh frame
        is [0 0 1]'

        Now all we need is the attitude of the body relative to the lvlh frame
        to get n_body = A_body_lvlh*n_lvlh
        """
        nadir = np.array([0, 0, 1])

        position_norm = norm(position)

        n = attitude_B_LVLH @ nadir

        n_cross = cross_product_matrix(n)

        return (3*self.mu/(position_norm**3))*(n_cross@(sc_inertia@n))
