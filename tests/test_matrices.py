from sim.math.matrices import cross_product_matrix
from numpy import array
from numpy import testing


def test_cross_product_matrix():
    vector = [0, 1, 3]
    testing.assert_allclose(cross_product_matrix(vector), array([
        [0, -3, 1],
        [3, 0, 0],
        [-1, 0, 0]
        ]))
