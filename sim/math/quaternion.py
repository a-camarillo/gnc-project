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
