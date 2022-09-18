#import numpy as np
import pandas as pd 

#import warnings

#warnings.filterwarnings('ignore')

URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv'




def carrega_dados(uri: str='') -> pd.DataFrame:
    if uri != '': 
        dados = pd.read_csv(uri, sep = ';') 
    else:
        return None

    return dados



if __name__ == '__main__':

    carrega_dados(URI) 
