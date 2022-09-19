import pandas as pd  
import numpy as np 
from src.aula_02 import carrega_dados, valores_unicos, frequencia

URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv'

def test_carrega_dados():

    recebi = type(carrega_dados(uri= URI, sep = ';' ))
    quero = pd.DataFrame 

    assert quero == recebi 

def test_valores_unicos():
    dados = carrega_dados(URI)

    recebi = valores_unicos(data_frame= dados, variavel='quality').tolist()
    recebi.sort()
    quero = [3,4,5,6,7,8]

    assert  recebi == quero


def test_frequencia():
    dados = carrega_dados(URI)

    recebi = frequencia(data_frame = dados, variavel = 'quality')
    
    d = {5: 681, 6: 638,  7:199, 4:53, 8:18, 3:10}
    quero = pd.Series(data=d, index= [3,4,5,6,7,8], name='quality')
    quero = quero.sort_values(ascending=False) 

    assert recebi.equals(quero) 

