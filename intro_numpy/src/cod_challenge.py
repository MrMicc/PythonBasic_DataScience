import numpy as np


#exercio 1 
def array_impares(quantidade: int = 1) -> np.ndarray:

    num = 1 
    lista = []

    while len(lista) < quantidade:
        if num % 2 == 0:
            lista.append(num)
        num +=1

    return np.array(lista)

if __name__ == '__main__':
    array_impares(4)


#exercicio 2
def array_dimensao(lista: list= ['1']) -> int:
    arr = np.array(lista)
    return arr.ndim 

