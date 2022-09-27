from src.cod_challenge import *

import numpy as np

def test_array_impares():
    recebi = array_impares(5)
    quero = np.array([2,4,6,8,10])

    #assert np.allclose(recebi, quero)

    assert all(recebi == quero)

