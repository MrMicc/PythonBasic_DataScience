from re import I
import pandas as pd
from src.hands_on import *


URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'


def test_carrega_dados():

    recebi = carrega_dados(URI)
    quero = pd.read_csv(URI)

    assert (recebi == quero).all


def test_retorna_formato():
    ds = carrega_dados(URI)
    recebi = retorna_formato(ds)

    quero = ds.shape

    assert recebi == quero


# Exercicio HandsOn2 - 1
def test_tx_crime_no_indice():
    recebi = tx_crime_no_indice(URI, index=9)

    quero = 55.30

    assert recebi == quero


# Exerccio Handon2 -2
def test_physicians_dado():

    recebi = physicians_dado(uri=URI, index=-1)

    quero = 140

    assert recebi == quero


# Exercicio Handon2 - 3
def test_new_label():

    recebi = new_label(
        uri=URI, index=[1, 3, 5, 7, 9, 13], columns=['land_area', 'work_force', 'income', 'region', 'crime_rate'])

    df = carrega_dados(URI)

    quero = df.loc[[1, 3, 5, 7, 9, 13], ['land_area',
                                         'work_force', 'income', 'region', 'crime_rate']]

    assert (recebi == quero).all


# Exerccio handson2 - 4
def test_quantidade_de_regiao_igual_a():

    recebi = quantidade_de_regiao_igual_a(uri=URI, valor=2)

    quero = 25

    assert recebi == quero


# Exercicio handson3 -1
def test_crime_rate_ordenado_descending():

    recebi = pegar_coluna_ordenado(
        uri=URI, quantidade=5, coluna='crime_rate', ascending=False)

    quero = 4

    assert recebi.region.iloc[0] == quero
