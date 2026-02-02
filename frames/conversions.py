import numpy as np
from numpy.linalg import cross, norm


def lvlh2inertial(r_I, v_I):
    """
    lvlh2inertial takes position and velocity vectors to get an attitude
    matrix from the lvlh frame to the inertial frame
    """
    # nadir vector
    o3 = -r_I / norm(r_I)

    # vector orthogonal to orbital plane (negative orbit normal)
    o2 = -(cross(r_I, v_I, axis=0)) / norm(cross(r_I, v_I, axis=0))

    # x-axis completing right hand triad
    o1 = cross(o2, o3)

    return np.concatenate((o1, o2, o3), axis=1)

