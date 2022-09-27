import numpy as np


def array_impares(quantidade: int = 1) -> int:

    num = 1 
    lista = []

    while len(lista) < quantidade:
        if num % 2 == 0:
            lista.append(num)
        num +=1

    return np.array(lista)

if __name__ == '__main__':
    array_impares(4)

    help(np.array)
