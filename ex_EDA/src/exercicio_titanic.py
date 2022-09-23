import numpy as np
import pandas as pd


URI = 'https://raw.githubusercontent.com/dphi-official/First_ML_Model/master/titanic.csv'

def carrega_data_set() -> pd.DataFrame:
    '''
        Função responsável em carregar o dataSet de um CSV e separar as colunas por ',' 

        Return
        --------
        pd.DatFrame -> Com dados do titanic 
    '''
    dados = pd.read_csv(URI, sep=',')

    return dados


def quantidade_de_dados_nulos(dados: pd.DataFrame, coluna: str) -> int:
    '''
        Função repsonsável por retornar a quantidade de nulos a partir de uma coluna do data set informado

        Parameters
        ----------
        dados: pd.DataFrame
        coluna: str


        Return
        ---------
        int -> quantidade de dados nulos
    '''
    return dados[coluna].isna().sum()


def conta_qtd_valores_na_coluna(dados: pd.DataFrame, coluna: str, valor: str) -> int:
    '''
        Função responsável em retornar a quantidade de valores em uma determinada coluna

        Parameters
        ----------
        dados: pd.DataFrame
        coluna: str 
        valor: str

        Return
        ---------
        int -> quantidade de valores repetidos
    '''
    return np.sum(dados[coluna] == valor )


def quantidade_de_passageiros_por_genero(dados: pd.DataFrame) -> dict:
    '''
        Função responsável por retornar um dicionário contendo a quantidade de passageiro por genero

        Paramters
        ---------
        dados: pd.DatFrame

        Return
        --------
        dict -> dicionário contendo a quantidade de passageiros por genero
    '''
    quantidade_por_genero = {}
    quantidade_por_genero['m'] = conta_qtd_valores_na_coluna(dados, 'Sex', 'male')  
    quantidade_por_genero['f'] = conta_qtd_valores_na_coluna(dados, 'Sex', 'female') 

    return quantidade_por_genero


def proporcao_coluna(dados: pd.DataFrame, coluna: str) -> float:
    '''
        Função reponsável em calcular a propoção de valores em uma determinada coluna e arredondar duas casas decimais

        Parameters
        ----------
        dados: pd.DatFrame
        coluna: str

        Return
        ---------
        float -> média 
    '''
    return round(dados[coluna].mean(),2)
