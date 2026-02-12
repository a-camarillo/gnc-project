import numpy as np
from typing import List


class Quaternion:
    def __init__(self,
                 array: np.array | List
                 ):

        # convert input to numpy array
        if type(array) is List:
            array = np.array(array)

        self.vector = array[0:3]
        self.scalar = array[3]

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
