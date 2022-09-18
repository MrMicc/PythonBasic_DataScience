import pandas as pd  
from src.aula_02 import carrega_dados 

URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv'

def test_carrega_dados():

    recebi = type(carrega_dados(uri= URI))
    quero = pd.DataFrame 

    assert quero == recebi 


