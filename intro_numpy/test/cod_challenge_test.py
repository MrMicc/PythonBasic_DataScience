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

def test_array_aleatorio():
    comeca_em = 17
    termina_em = 31
    quantidade_intervalos = 50 
    recebi = array_aleatorio(comeca_em = comeca_em, termina_em = termina_em, qtd_intervalos = quantidade_intervalos)

    quero = np.array([17, 17.28571429, 17.57142857, 17.85714286, 18.14285714, 18.42857143, 18.71428571, 19., 19.28571429, 19.57142857, 19.85714286, 20.14285714,
                     20.42857143, 20.71428571, 21., 21.28571429, 21.57142857, 21.85714286, 22.14285714, 22.42857143, 22.71428571, 23., 23.28571429, 23.57142857,
                     23.85714286, 24.14285714, 24.42857143, 24.71428571, 25., 25.28571429, 25.57142857, 25.85714286, 26.14285714, 26.42857143, 26.71428571, 27.,
                     27.28571429, 27.57142857, 27.85714286, 28.14285714, 28.42857143, 28.71428571, 29., 29.28571429, 29.57142857, 29.85714286, 30.14285714,
                     30.42857143, 30.71428571, 31.])
    assert all(recebi == quero)


def test_array_ordena_e_deleta():

    lista = [10, 2, 7, 8, 3, 22, 54, 12, 13, 46, 23, 25, 41]

    recebi = array_ordena_e_deleta(lista, deleta_posicao=4)
    quero = np.array([2,  3,  7,  8, 12, 13, 22, 23, 25, 41, 46, 54])
    print(recebi)

    assert all(recebi == quero) 
