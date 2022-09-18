#import numpy as np
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



if __name__ == '__main__':

    carrega_dados(URI) 
