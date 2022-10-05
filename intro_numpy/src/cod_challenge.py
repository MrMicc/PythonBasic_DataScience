import numpy as np


#exercicio 1 
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


#exercicio 3 
def array_aleatorio(comeca_em: int = 1, termina_em: int = 10, qtd_intervalos = 5, qtd_casas_decimais_nos_intervalos = 8):

    arr =  np.linspace(start = comeca_em, stop = termina_em, num = qtd_intervalos)
    arr_arrendondado = [] 

    for x in arr: 
        arr_arrendondado = np.append(arr_arrendondado, round(x, qtd_casas_decimais_nos_intervalos))

    return arr_arrendondado 
