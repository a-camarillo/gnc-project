import numpy as np

# Newton's Gravitational Constant
G = 6.6743*(10**-11)

# Earth's mass in kg
M = 5.972*(10**24)

# Gravitational Parameter mu
EARTH_MU = G*M

# radius of Earth in meters
EARTH_RADIUS = 6_371*(10**3)

# Moment of Inertia
J_SC = np.array([
    [180, 0, 0],
    [0, 160, 0],
    [0, 0, 80],
])

# WGS84 Constants #

# Earth's semimajor axis in m
WGS_EARTH_SEMIMAJOR_AXIS = 6_378_137.0

# Earth's semiminor axis in m
WGS_EARTH_SEMIMINOR_AXIS = 6_356_752.3142

# Earth's flattening
WGS_FLATTENING = 1/298.257

# eccentricity
WGS_ECCENTRICITY = 0.0818
