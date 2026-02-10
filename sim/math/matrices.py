import numpy as np
from typing import List


def cross_product_matrix(
        vector: np.array | List
        ):
    """
    cross_product_matrix takes in a 3x1 or 1x3 vector and returns a 3x3
    skew-symmetric matrix
    """
    if type(vector) is List:
        vector = np.array(vector)

    return np.array([
        [ 0, -vector[2], vector[1] ],
        [ vector[2], 0, -vector[0] ],
        [ -vector[1], vector[0], 0 ],
    ])
