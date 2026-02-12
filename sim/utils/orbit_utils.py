from math import cos, acos, degrees, sin
from numpy.linalg import norm, cross, vecdot
from sim.frames.conversions import perifocal2ijk
import numpy as np
from sim.utils.constants import EARTH_MU


def rv2coe(position, velocity, mu):
    """
    Calculate the classical orbital elements from position and velocity vector
    """
    # Take magnitudes of position and velocity vectors
    r = norm(position)
    v = norm(velocity)

    # Get specific angular momentum
    h_vec = cross(position, velocity)
    h = norm(h_vec)

    # calculate the node vector

    # Unit Vector for K axis of IJK reference system
    K_vec = np.array([
                [0],
                [0],
                [1],
    ])
    n_vec = cross(K_vec, h_vec)
    n = norm(n_vec)

    # eccentricity
    e_vec = 1/mu*((v**2 - mu/r)*position -
                  (vecdot(position, velocity)*velocity))

    ecc = norm(e_vec)

    # specific mechanical energy
    ksi = (v**2)/2 - mu/r

    # check eccentricity
    if ecc < 1.0 and ecc > 0.0:
        # get semi-major axis from specific mechanical energy
        a = -mu/(2*ksi)
        # get semi-parameter
        p = a*(1-ecc**2)

    inc = degrees(acos(h_vec[2, 0]/h))
    RAAN = degrees(acos(n_vec[0, 0]/n))
    if n_vec[1, 0] < 0.0:
        RAAN = 360.0 - RAAN

    argp = degrees(acos((vecdot(n_vec, e_vec))/(n*ecc)))
    if e_vec[2, 0] < 0.0:
        argp = 360.0 - argp

    nu = degrees(acos(vecdot(e_vec, position)/(ecc*r)))
    if vecdot(position, velocity) < 0.0:
        nu = 360.0 - nu

    return p, a, ecc, inc, RAAN, argp, nu


def coe2rv(p, ecc, inc, RAAN, argp, nu):
    """
    Calculate the position and velocity vector from the classical
    orbital elements
    """

    # position and velocity in perifocal coordinates
    position_PQW = np.array([
        [(p*cos(nu))/(1+ecc*cos(nu))],
        [(p*sin(nu))/(1+ecc*cos(nu))],
        [0],
    ])

    velocity_PQW = np.array([
        [-((EARTH_MU/p)**0.5)*(sin(nu))],
        [((EARTH_MU/p)**0.5)*(ecc + cos(nu))],
        [0],
    ])

    position_IJK = perifocal2ijk(RAAN, argp, inc) @ position_PQW
    velocity_IJK = perifocal2ijk(RAAN, argp, inc) @ velocity_PQW

    position_IJK = position_IJK.reshape(-1)
    velocity_IJK = velocity_IJK.reshape(-1)

    return position_IJK, velocity_IJK
