import pandas as pd
from src.hands_on import *


URI = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'

def test_carrega_dados():

    recebi = carrega_dados(URI, ',')
    quero = pd.read_csv(URI)

    assert  (recebi == quero).all


def test_retorna_formato():
    ds = carrega_dados(URI)
    recebi = retorna_formato(ds)

    quero = ds.shape


    assert recebi == quero
