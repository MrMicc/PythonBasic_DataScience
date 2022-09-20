import numpy as np
import pandas as pd 

#import warnings

#warnings.filterwarnings('ignore')

URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv'




def carrega_dados(uri: str='', sep = ';') -> pd.DataFrame:
    '''
        função responsável por carregar uma base em csv a partir de uma URI e separar a partir de uma parametro 

        Parameters
        __________
        uri: str
        sep: str -> ';'

        Return
        ---------
        Pandas DataFrame 
    '''
    if uri != '': 
        dados = pd.read_csv(uri, sep = sep) 
    else:
        return None

    return dados


def valores_unicos(data_frame: pd.DataFrame, variavel: str= 'quality'):
    '''função responsável por retornar os valores únicos de uma determinada variavel em um DataFrame
        
        Parameters
        ----------
        data_frame: DataFrame 
        varavel: str -> quality
        
        Return
        ---------
        array 
    '''

    return  data_frame[variavel].unique()






def frequencia(data_frame: pd.DataFrame, variavel = 'quality'):
    '''Função responsável por retonar a frequencia de valores de uma determinada variavel em um DataFrame

        Parameters
        ----------
        data_frame: DataFrame
        variavel: str -> quality

        Return
        --------
        Panda Serie
    '''
    return data_frame[variavel].value_counts()     



def troca_espaco_para_underline(com_espaco: str = '') -> str:
    '''
        Função responsável em retornar uma string trocando o char espaço (' ') por underline ('_')

        Parameters
        ----------
        com_espaco: str

        Return
        ----------
        str -> Sem espaço
    '''
    return com_espaco.replace(' ', '_')




def tira_espaco_de_colunas(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Funcão responsável em retirar os espaços (' ') dos nomes das colunas de um DataFrame e substituir por underline ('_')

        Parameters
        ----------
        df: Pandas DataFrame

        Return
        ----------
        Pandas DataFrame
    '''

    colunas = {}

    for coluna_com_espaco in df.columns:
        coluna_sem_espaco = troca_espaco_para_underline(coluna_com_espaco)
        colunas.update({coluna_com_espaco: coluna_sem_espaco})

    df.rename(columns = colunas, inplace = True)
    
    return df
    





if __name__ == '__main__':

    dados = carrega_dados(URI)
    print(dados.columns)



    print('Analise quai são os votos de qualidade dos vinhos:')
    print(valores_unicos(data_frame = dados, variavel = 'quality'))
    print('Frequencia de que cada voto foi dado')
    print(frequencia(data_frame=dados, variavel= 'quality')) 
    
    print ('Ajustando o nome das colunas')
    print(f'Antes: {dados.columns}')
    dados = tira_espaco_de_colunas(dados)
    print(f'\n\nDepois: {dados.columns}') 





