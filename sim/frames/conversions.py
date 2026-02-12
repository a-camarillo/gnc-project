import numpy as np
from math import cos, sin
from numpy.linalg import cross, norm


def lvlh2inertial(position, velocity):
    """
    lvlh2inertial takes position and velocity vectors to get an attitude
    matrix from the lvlh frame to the inertial frame
    """
    # nadir vector
    o3 = -position / norm(position)

    # vector orthogonal to orbital plane (negative orbit normal)
    o2 = -(cross(position, velocity)) / norm(cross(position, velocity))

    # x-axis completing right hand triad
    o1 = cross(o2, o3)

    return np.column_stack((o1, o2, o3))


def perifocal2ijk(RAAN, argp, inc):
    return np.array([
        [cos(RAAN)*cos(argp)-sin(RAAN)*sin(argp)*cos(inc),
         -cos(RAAN)*sin(argp)-sin(RAAN)*cos(argp)*cos(inc),
         sin(RAAN)*sin(inc)],
        [sin(RAAN)*cos(argp)+cos(RAAN)*sin(argp)*cos(inc),
         -sin(RAAN)*sin(argp)+cos(RAAN)*cos(argp)*cos(inc),
         -cos(RAAN)*sin(inc)],
        [sin(argp)*sin(inc), cos(argp)*sin(inc), cos(inc)]
    ])
