from sim.utils.constants import EARTH_MU, EARTH_RADIUS


class Environment:
    def __init__(self):
        # gravitational parameter
        self.mu = EARTH_MU
        # radius of Earth in m
        self.r_earth = EARTH_RADIUS
