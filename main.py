from sim.dynamics.attitude import AttitudeModel
from sim.dynamics.orbit import OrbitModel
from sim.dynamics.spacecraft import SpaceCraftModel
from sim.math.ode import rk4_step
from sim.math.quaternion import Quaternion
from sim.utils.orbit_utils import coe2rv
from sim.utils.clock import SimulationClock
from sim.environment import gravity, magnetic
from math import radians
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    sim_time = 3600*4
    plant_time = 0.0
    plant_dt = 0.01
    epoch = datetime(2025, 1, 1, 0, 0, 0, 0)
    clock = SimulationClock(epoch)

    spacecraft_inertia = np.array([
        [180, 0, 0],
        [0, 130, 0],
        [0, 0, 100],
    ])

    # semi-parameter
    p = 500*(10**3)
    # right argument of the ascending node
    RAAN = radians(40)
    # inclination
    inc = radians(54.7)
    # eccentricity
    ecc = 0.8
    # argument of periapsis
    argp = radians(50)
    # true anomaly
    nu = radians(0)

    position0, velocity0 = coe2rv(p, ecc, inc, RAAN, argp, nu)
    position0_x = position0[0]
    position0_y = position0[1]
    position0_z = position0[2]
    velocity0_x = velocity0[0]
    velocity0_y = velocity0[1]
    velocity0_z = velocity0[2]

    attitude = AttitudeModel(spacecraft_inertia)
    orbit = OrbitModel()
    grav_field = gravity.GravityField()
    mag_field = magnetic.MagneticField()

    steps = int(sim_time/plant_dt)
    sim_steps = 0
    states = np.zeros((13, steps))

    states[:, 0] = np.array([position0_x, position0_y, position0_z,
                             velocity0_x, velocity0_y, velocity0_z,
                             0, 0, 0, 1, 0.1, 0.1, 0.1])

    spacecraft = SpaceCraftModel(attitude_model=attitude, orbit_model=orbit,
                                 environments=[mag_field, grav_field])

    while sim_steps < steps:
        if sim_steps == (steps-1):
            break
        if (clock.t % 1) == 0:
            mag_field.calculate_mag_field_body(
                    position_inertial=states[0:3, sim_steps],
                    attitude=Quaternion(states[6:10, sim_steps]),
                    date=clock.datetime()
            )
        states[:, sim_steps+1] = rk4_step(spacecraft.propagate,
                                          plant_time,
                                          states[:, sim_steps],
                                          plant_dt)
        clock.step(plant_dt)
        sim_steps += 1

    time = np.arange(0, sim_time, plant_dt)

    fig = plt.figure(tight_layout=True)

    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax1.plot(time, states[10, :])
    ax2.plot(time, states[11, :])
    ax3.plot(time, states[12, :])

    fig2 = plt.figure()
    ax4 = fig2.add_subplot(111, projection='3d')
    ax4.plot(states[0, :], states[1, :], states[2, :])

    plt.show()


if __name__ == "__main__":
    main()
