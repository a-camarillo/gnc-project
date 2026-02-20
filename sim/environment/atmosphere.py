from sim.environment.environment import Environment
from sim.environment.exponential_atmosphere_table import table
from sim.utils.constants import WGS_EARTH_SEMIMAJOR_AXIS as earth_radius
from numpy.linalg import norm


class Atmosphere(Environment):
    def __init__(self):
        super().__init__()
        self.exponential_table = table

    def calculate_air_density(self, position_inertial):
        position = norm(position_inertial)

        # get altitude in meters
        altitude = position - earth_radius

        # convert altitude to km
        altitude_km = altitude*(10**-3)
        match altitude_km:
            case altitude_km if altitude_km in range(0, 25):
                base_altitude = self.exponential_table["0-25"]["base_altitude"]
                nominal_density = (self.exponential_table["0-25"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["0-25"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(25, 30):
                base_altitude = (self.exponential_table["25-30"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["25-30"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["25-30"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(30, 40):
                base_altitude = (self.exponential_table["30-40"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["30-40"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["30-40"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(40, 50):
                base_altitude = (self.exponential_table["40-50"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["40-50"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["40-50"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(50, 60):
                base_altitude = (self.exponential_table["50-60"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["50-60"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["50-60"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(60, 70):
                base_altitude = (self.exponential_table["60-70"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["60-70"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["60-70"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(70, 80):
                base_altitude = (self.exponential_table["70-80"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["70-80"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["70-80"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(80, 90):
                base_altitude = (self.exponential_table["80-90"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["80-90"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["80-90"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(90, 100):
                base_altitude = (self.exponential_table["90-100"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["90-100"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["90-100"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(100, 110):
                base_altitude = (self.exponential_table["100-110"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["100-110"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["100-110"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(110, 120):
                base_altitude = (self.exponential_table["110-120"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["110-120"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["110-120"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(120, 130):
                base_altitude = (self.exponential_table["120-130"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["120-130"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["120-130"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(130, 140):
                base_altitude = (self.exponential_table["130-140"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["130-140"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["130-140"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(140, 150):
                base_altitude = (self.exponential_table["140-150"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["140-150"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["140-150"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(150, 180):
                base_altitude = (self.exponential_table["150-180"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["150-180"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["150-180"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(180, 200):
                base_altitude = (self.exponential_table["180-200"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["180-200"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["180-200"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(200, 250):
                base_altitude = (self.exponential_table["200-250"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["200-250"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["200-250"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(250, 300):
                base_altitude = (self.exponential_table["250-300"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["250-300"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["250-300"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(300, 350):
                base_altitude = (self.exponential_table["300-350"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["300-350"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["300-350"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(350, 400):
                base_altitude = (self.exponential_table["350-400"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["350-400"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["350-400"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(450, 500):
                base_altitude = (self.exponential_table["450-500"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["450-500"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["450-500"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(500, 600):
                base_altitude = (self.exponential_table["500-600"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["500-600"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["500-600"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(600, 700):
                base_altitude = (self.exponential_table["600-700"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["600-700"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["600-700"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(700, 800):
                base_altitude = (self.exponential_table["700-800"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["700-800"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["700-800"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(800, 900):
                base_altitude = (self.exponential_table["800-900"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["800-900"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["800-900"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km in range(900, 1000):
                base_altitude = (self.exponential_table["900-1000"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["900-1000"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["900-1000"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
            case altitude_km if altitude_km >= 1000:
                base_altitude = (self.exponential_table["1000"]
                                 ["base_altitude"])
                nominal_density = (self.exponential_table["1000"]
                                   ["nominal_density"])
                scale_height = (self.exponential_table["1000"]
                                ["scale_height"])
                density = (nominal_density ** (
                    -(altitude_km - base_altitude)/scale_height))
                return density
