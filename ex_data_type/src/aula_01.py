def soma(x: int=0, y: int=0) -> int:
    '''Soma de dois numeros inteiros
        
        Parameters
        ----------
        x: int
        y: int
    ''' 

    return x+y

def cubo()-> int:
    '''Faz o calculo de um numero inteiro ao cubo ao ser inserido pelo input'''

    numero = int(input('Numero a ser elevado ao cubo:'))
    
    return numero**3


def subtrai_total_duas_listas(l1: list = [0], l2: list = [0]) -> int:
    '''Realiza a soma de duas listas inteiras
        
        Parameters
        ----------
        l1: list 
        l2: list

        Return
        ---------
        int 
    ''' 

    soma_l1 = sum(l1)
    soma_l2 = sum(l2)

    return soma_l1 - soma_l2 
