from src.exercicio_titanic import carrega_data_set, quantidade_de_dados_nulos, quantidade_de_passageiros_por_genero, proporcao_coluna,calcula_percentil_de_sobreviventes_por_genero, calcula_percentil_sobreviventes_por_classe, calcula_percentil_sobreviventes_por_idade,  retorna_quantil
import math
import numpy as np

DADOS = carrega_data_set()



def test_quantidade_de_dados_nulos():
    '''
        Teste de quantidade de nulos em uma determinada coluna 
        Teste sendo realizado na colua FARE
    '''
    recebi = quantidade_de_dados_nulos(DADOS,coluna='Fare')
    quero = 0

    assert recebi == quero



def test_quantidade_de_passageiros_por_genero():
    '''
        Teste de quantidade de passageiro por genero
    '''
    recebi = quantidade_de_passageiros_por_genero(DADOS)
    quero = {'female':314, 'male':577}
    
    print(recebi)
    assert quero == recebi


def test_proprocao_coluna():
    '''
        Função que teste a média/propoção de uma determinada coluna
        Teste sendo realizado na coluna Survived
    '''
    recebi = proporcao_coluna(DADOS, 'Survived')
    quero = 0.38

    assert quero == recebi


def test_proprocao_coluna_fare():
    recebi = retorna_quantil(DADOS, 'Fare') 
    quero = 14.4542 

    assert quero == recebi #math.isclose(recebi, quero) 


def test_calcula_percentil_de_sobreviventes_por_genero():
    recebi = calcula_percentil_de_sobreviventes_por_genero(DADOS)
    quero = {'female': 74.20, 'male': 18.89}

    assert quero == recebi 


def test_calcula_percentil_sobreviventes_por_classe():
    recebi = calcula_percentil_sobreviventes_por_classe(DADOS)
    quero =  {1: 62.96, 2: 47.28, 3: 24.24} 


    assert quero == recebi




def test_caclula_percentil_sobreviventes_por_idade():
    recebi = calcula_percentil_sobreviventes_por_idade(DADOS)
    quero = {'Maior idade': 38.10, 'Menor idade': 53.98}

    assert quero == recebi

