import numpy as np
import pandas as pd


URI = 'https://raw.githubusercontent.com/dphi-official/First_ML_Model/master/titanic.csv'

def carrega_data_set() -> pd.DataFrame:
    dados = pd.read_csv(URI, sep=',')

    return dados


def quantidade_de_dados_nulos(dados: pd.DataFrame, coluna: str) -> int:
    return dados[coluna].isna().sum()


def conta_qtd_valores_na_coluna(dados: pd.DataFrame, coluna: str, valor: str) -> int:
    return np.sum(dados[coluna] == valor )


def quantidade_de_passageiros_por_genero(dados: pd.DataFrame) -> dict:
    quantidade_por_genero = {}
    quantidade_por_genero['m'] = conta_qtd_valores_na_coluna(dados, 'Sex', 'male')  
    quantidade_por_genero['f'] = conta_qtd_valores_na_coluna(dados, 'Sex', 'female') 



    return quantidade_por_genero


