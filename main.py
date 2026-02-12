from sim.dynamics.attitude import AttitudeModel
from sim.dynamics.orbit import OrbitModel
from sim.dynamics.spacecraft import SpaceCraftModel
from sim.utils.constants import EARTH_MU, EARTH_RADIUS
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def rk4_step(f, t, x, dt):
    # rk4_step
    k1 = f(t, x)
    k2 = f(t+0.5*dt, x+0.5*dt*k1)
    k3 = f(t+0.5*dt, x+0.5*dt*k2)
    k4 = f(t+dt, x+dt*k3)
    return x + (dt/6)*(k1+2*k2+2*k3+k4)


def main():
    sim_time = 3600
    plant_time = 0.0
    plant_dt = 0.01

    spacecraft_inertia = np.array([
        [180, 0, 0],
        [0, 130, 0],
        [0, 0, 100],
    ])

    attitude = AttitudeModel(spacecraft_inertia)
    orbit = OrbitModel()

    steps = int(sim_time/plant_dt)
    sim_steps = 0
    states = np.zeros((13, steps))

    position0 = EARTH_RADIUS + 400*(10**3)
    velocity0 = (EARTH_MU/position0)**0.5

    states[:, 0] = np.array([position0, 0, 0, 0, velocity0, 0,
                             0, 0, 0, 1, 0.1, 0.1, 0.1])

    spacecraft = SpaceCraftModel(attitude_model=attitude, orbit_model=orbit)

    while sim_steps < steps:
        if sim_steps == (steps-1):
            break
        states[:, sim_steps+1] = rk4_step(spacecraft.propagate,
                                          plant_time,
                                          states[:, sim_steps],
                                          plant_dt)
        plant_time += plant_dt
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
