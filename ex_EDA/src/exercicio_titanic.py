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

    return retorna_dicionario_da_coluna(dados, 'Sex')


def proporcao_coluna(dados: pd.DataFrame, coluna: str, decimal: int = 2) -> float:
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
    return round(dados[coluna].mean(),decimal)

def retorna_quantil(dados: pd.DataFrame, coluna: str, quantil: float = 0.5) -> float:

    return dados[coluna].quantile(0.5)


def realiza_calculo_porcentagem(quantidade_total: dict, quantidade_final: dict) -> dict:
    '''
        Função especializada em realizar calculo de percentil a partir de um dicionário e retornar um dicionário com as mesmas chaves e seus valores em
        percentil

        Parameters
        -----------
        quantidade_total: dict
        quantidade_final: dict

        Returns
        -----------
        dict -> Contendo as chave passadas e seus valores em percentil 
    '''
    total = {}
   
    for key, value in quantidade_total.items():
        total[key] = round((quantidade_final[key]/value)*100,2)

    return total

def calcula_percentil_de_sobreviventes_por_genero(dados: pd.DataFrame) -> dict:
    '''
        Função responsável em retornar o percentil de sobreviventes por genero e retornar através de um dicionário

        Parameters
        -----------
        dados: pd.DataFrame

        Return
        dict -> contendo dois generos e seus valores em % com duas casas decimais 
    '''
    total_passageiros_por_genero = quantidade_de_passageiros_por_genero(dados)
    
    total_passageiros_por_genero_sobreviventes = quantidade_de_passageiros_por_genero(dados[dados['Survived'].isin([1])])


    return realiza_calculo_porcentagem(total_passageiros_por_genero, total_passageiros_por_genero_sobreviventes)

def retorna_dicionario_da_coluna(dados: pd.DataFrame, coluna: str) ->dict:
    dicionario = {}
    print(dados[coluna].unique())

    for key in dados[coluna].unique():
        dicionario[key] = conta_qtd_valores_na_coluna(dados,coluna,key)
    
    return dicionario 



def calcula_percentil_sobreviventes_por_classe(dados: pd.DataFrame) -> dict:
    
    dict_classes_total = retorna_dicionario_da_coluna(dados, 'Pclass')
    
    dict_classes_sobreviventes = retorna_dicionario_da_coluna(dados[dados['Survived'].isin([1])], 'Pclass')

    return realiza_calculo_porcentagem(dict_classes_total, dict_classes_sobreviventes)

def calcula_percentil_sobreviventes_por_idade(dados: pd.DataFrame) -> dict:
    
    dict_maior_menor_idade = {} 
    dict_maior_menor_idade['Menor idade'] = round(np.mean(dados['Survived'][dados['Age'] < 18])*100,2)
    dict_maior_menor_idade['Maior idade'] = round(np.mean(dados['Survived'][dados['Age'] >= 18])*100,2) 

    return dict_maior_menor_idade


def quantidade_de_sobrevivente_por_embarque(dados: pd.DataFrame) -> dict:

    dados_sobreviventes =  dados[dados['Survived'] == 1]

    embarque = {}
    embarque = dados_sobreviventes['Embarked'].value_counts()

    return embarque.to_dict()



def retorna_tarifas(dados: pd.DataFrame, crescente:bool = True, quantidade:int = 0) -> list:
    if (quantidade <= 0):
        return list(dados['Fare'].sort_values(ascending= crescente))
    else: 
        return list(dados['Fare'].sort_values(ascending = crescente))[:quantidade]





def mediana_idade_passageiros(dados: pd.DataFrame) -> int:

    df_idade = dados[dados['Age']>=0]

    return round(df_idade['Age'].median())



def recupera_quantidade_nomes_unicos(dados: pd.DataFrame) -> int:
    return len(dados['Name'].unique())
