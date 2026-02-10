from math import cos, acos
from numpy.linalg import norm, cross

def rv2coe(r_vec, v_vec, mu):
    """
    Calculate the classical orbital elements from position and velocity vector
    """
    # Take magnitudes of position and velocity vectors
    r = norm(r_vec)
    v = norm(v_vec)

    # Get specific angular momentum
    h_vec = cross_product(r_vec, v_vec)
    h = norm(h_vec)

    # calculate the node vector

    # Unit Vector for K axis of IJK reference system
    K_vec = np.array([
                [0],
                [0],
                [1],
    ])
    n_vec = cross_product(K_vec, h_vec)
    n = norm(n_vec)

    # eccentricity
    e_vec = 1/mu*((v**2 - mu/r)*r_vec - (inner_product(r_vec, v_vec)*v_vec))

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

    argp = degrees(acos((inner_product(n_vec, e_vec))/(n*ecc)))
    if e_vec[2, 0] < 0.0:
        argp = 360.0 - argp

    nu = degrees(acos(inner_product(e_vec, r_vec)/(ecc*r)))
    if inner_product(r_vec, v_vec) < 0.0:
        nu = 360.0 - nu

    return p, a, ecc, inc, RAAN, argp, nu
