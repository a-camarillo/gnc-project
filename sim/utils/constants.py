import numpy as np

# Newton's Gravitational Constant
G = 6.6743*(10**-11)

# Earth's mass in kg
M = 5.972*(10**24)

# Gravitational Parameter mu
EARTH_MU = G*M

# radius of Earth
EARTH_RADIUS = 6371*(10**3)

# Moment of Inertia
J_SC = np.array([
    [180, 0, 0],
    [0, 160, 0],
    [0, 0, 80],
])
