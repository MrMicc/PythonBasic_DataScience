from src.exercicio_titanic import * 
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



def test_quantidade_de_sobreviventes_por_emarque():
    recebi = quantidade_de_sobrevivente_por_embarque(DADOS)
    quero = 217 

    assert quero == recebi['S']





def test_retorna_tarifas():
    recebi = retorna_tarifas(DADOS, crescente = False, quantidade = 5)
    quero = [512.3292, 512.3292, 512.3292, 263.0, 263.0]

    assert quero == recebi





def test_mediana_idade_passageiros():
    recebi = mediana_idade_passageiros(DADOS)
    quero = 28

    assert quero == recebi


def test_recupera_quantidade_nomes_unicos():

    recebi = recupera_quantidade_nomes_unicos(DADOS)

    quero = 891

    assert quero == recebi


def test_recupera_quantidade_de_irmao_ou_esposa():
    recebi = recupera_quantidade_de_irmao_ou_esposa(DADOS)
    
    quero = {0: 608, 1:209, 2:28, 3:16, 4:18, 5:5, 8:7}

    assert quero == recebi








