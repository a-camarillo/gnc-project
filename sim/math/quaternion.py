import numpy as np
from typing import List


class Quaternion:
    def __init__(self,
                 array: np.array | List
                 ):

        # convert input to numpy array
        if isinstance(array, list):
            array = np.array(array)

        self.vector = array[0:3]
        self.scalar = array[3]
        self._array = array

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(Vector={self.vector},'
            f' Scalar={self.scalar})'
        )

    def __array__(self, dtype=None, copy=None):
        if copy is False:
            raise ValueError(
                    "`copy=False` isn't supported. A copy is always created."
                )
        return np.array(self._array)

    def quaternion2rotation_matrix(self):
        q1 = self.vector[0]
        q2 = self.vector[1]
        q3 = self.vector[2]
        q4 = self.scalar
        return np.array([
            [(q1**2 - q2**2 - q3**2 + q4**2),
             (2*(q1*q2 + q3*q4)),
             (2*(q1*q3 - q2*q4))],
            [(2*(q2*q1 - q3*q4)),
             (-q1**2 + q2**2 - q3**2 + q4**2),
             (2*(q2*q3 + q1*q4))],
            [(2*(q3*q1 + q2*q4)),
             (2*(q3*q2 - q1*q4)),
             (-q1**2 - q2**2 + q3**2 + q4**2)],
        ])
