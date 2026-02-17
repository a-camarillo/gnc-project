import numpy as np
from math import cos, sin, asin, atan2
from numpy.linalg import cross, norm
from sim.utils.constants import WGS_ECCENTRICITY, WGS_EARTH_SEMIMAJOR_AXIS
from sim.utils.constatns import WGS_EARTH_SEMIMINOR_AXIS


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


def geod2ecef(longitude, latitude, height):
    """
    calculate ECEF position vector from geodetic coordinates
    """
    longitude = np.deg2rad(longitude)
    latitude = np.deg2rad(latitude)
    N = (WGS_EARTH_SEMIMAJOR_AXIS /
         (1 - (WGS_ECCENTRICITY**2)*(sin(latitude))**2)**0.5)

    position_x = (N+height)*cos(latitude)*cos(longitude)
    position_y = (N+height)*cos(latitude)*sin(longitude)
    position_z = (N*(1-WGS_ECCENTRICITY**2)+height)*sin(latitude)

    position_ecef = [position_x, position_y, position_z]
    return position_ecef


def ecef2geod(position_ecef):
    """
    calculate geodetic latitude, longitude, and height from ecef position
    """
    x = position_ecef[0]
    y = position_ecef[1]
    z = position_ecef[2]

    e2 = 1 - (WGS_EARTH_SEMIMINOR_AXIS**2/WGS_EARTH_SEMIMAJOR_AXIS**2)
    epsilon2 = (WGS_EARTH_SEMIMAJOR_AXIS**2/WGS_EARTH_SEMIMINOR_AXIS**2) - 1

    rho = (x**2 + y**2)**0.5
    p = abs(z)/epsilon2
    s = (rho**2)/(e2*epsilon2)
    q = p**2 - WGS_EARTH_SEMIMINOR_AXIS**2 + s
    u = p/(q**0.5)
    v = ((WGS_EARTH_SEMIMINOR_AXIS**2)*(u**2))/q
    P = (27*v*s)/q
    Q = ((P+1)**0.5 + P**0.5)**(2/3)
    t = (1 + Q + 1/Q)/6
    c = (u**2 - 1 + 2*t)**0.5
    w = (c-u)/2
    d = np.sign(z)*(q**0.5)*(
            w + ((t**2+v)**0.5 - (u*w) - (t/2) - (1/4))**0.5)
    N = WGS_EARTH_SEMIMAJOR_AXIS*(
            1+epsilon2*(d**2)/(WGS_EARTH_SEMIMINOR_AXIS**2))**0.5
    latitude = asin((epsilon2 + 1)*(d/N))
    height = (rho*cos(latitude) + z*sin(latitude) -
              (WGS_EARTH_SEMIMAJOR_AXIS**2)/N)
    longitude = atan2(y, x)
    return latitude, longitude, height
