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


def array_ordena_e_deleta(lista: list, deleta_posicao: int) -> np.ndarray:

    return np.delete(np.sort(lista), deleta_posicao)



def refazendo_array(lista, eixo_x, eixo_y):

    return np.reshape(lista,(eixo_x, eixo_y))

#exercicio 5a

def criar_array(quantidade:int = 1, qtd_coluna = 1, qtd_linha = 1) ->  np.ndarray:
    arr = np.arange(start=0, stop= quantidade, step = 1)

    arr = arr.reshape(qtd_linha, qtd_coluna)
    
    return arr




if __name__ == '__main__':
    arr = criar_array(quantidade=25, qtd_linha=5, qtd_coluna=5)
    print(arr)

    print('------next----')
    print(arr[:2,3:])

    print('-----next-----')
    print(arr[1::2, ::2])
