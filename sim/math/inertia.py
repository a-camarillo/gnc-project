from numpy import array


def calculate_rectangular_moment_of_inertia(
        x_dimension: float,
        y_dimension: float,
        z_dimension: float,
        mass: float,
        ) -> array:
    I_xx = (1/12)*mass*(y_dimension**2 + z_dimension**2)
    I_yy = (1/12)*mass*(x_dimension**2 + z_dimension**2)
    I_zz = (1/12)*mass*(x_dimension**2 + y_dimension**2)
    return array([
        [I_xx, 0., 0.],
        [0., I_yy, 0.],
        [0., 0., I_zz]
    ])
