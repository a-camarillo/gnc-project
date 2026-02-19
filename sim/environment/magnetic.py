import numpy as np
import ppigrf
from datetime import datetime
from numpy import rad2deg
from sim.environment.environment import Environment
from sim.frames.conversions import inertial2ecef, ecef2geod, ecef2enu
from sim.math.time import calculate_gmst_angle
from sim.math.quaternion import Quaternion


class MagneticField(Environment):
    def __init__(self):
        super().__init__()
        self.mag_body = np.array([0, 0, 0])

    def calculate_mag_field_body(self,
                                 attitude: Quaternion,
                                 position_inertial,
                                 date: datetime):
        gmst_angle = calculate_gmst_angle(date)
        R_ECEF_INERTIAL = inertial2ecef(gmst_angle)
        position_inertial = position_inertial.reshape(-1, 1)
        position_ecef = R_ECEF_INERTIAL @ position_inertial
        lat, lon, height = ecef2geod(position_ecef)
        # igrf latitude and longitude needs to be in degrees
        lat_deg = rad2deg(lat)
        lon_deg = rad2deg(lon)
        # get magnetic field strength in ENU frame
        mag_E, mag_N, mag_U = ppigrf.igrf(lat_deg, lon_deg, height, date)
        # create magnetic field vector, convert from nT
        mag_enu = np.array([
            [mag_E[0][0]*(10**-9)],
            [mag_N[0][0]*(10**-9)],
            [mag_U[0][0]*(10**-9)]
        ])

        # get magnetic field vector in ECEF
        R_ECEF_ENU = ecef2enu(lat, lon).T
        mag_ecef = R_ECEF_ENU @ mag_enu

        # convert to inertial frame
        R_INERTIAL_ECEF = R_ECEF_INERTIAL.T
        mag_inertial = R_INERTIAL_ECEF @ mag_ecef

        # inertial to body frame rotation matrix
        R_BODY_INERTIAL = attitude.quaternion2rotation_matrix()

        # convert to body frame
        mag_body = R_BODY_INERTIAL @ mag_inertial

        self.mag_body = mag_body
