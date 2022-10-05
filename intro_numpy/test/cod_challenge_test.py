from src.cod_challenge import *

import numpy as np

def test_array_impares():
    recebi = array_impares(5)
    quero = np.array([2,4,6,8,10])

    #assert np.allclose(recebi, quero)

    assert all(recebi == quero)

#exercicio 2
def test_dimensao():
    lista = [2, 5, 8, 6, 4, 12, 16, 15]
    recebi = array_dimensao(lista)

    quero = 1

    assert recebi == quero 
