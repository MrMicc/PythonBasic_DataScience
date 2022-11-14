import pandas as pd
from pandas.core.api import Series
from pandas.core.frame import Dtype


def carrega_dados(uri: str) -> pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=uri)  # type: ignore


def retorna_formato(ds: pd.Series):

    return ds.shape


def tx_crime_no_indice(uri: str, index: int) -> float:

    df = carrega_dados(uri=uri)

    return (df.crime_rate.iloc[index])


def physicians_dado(uri: str, index: int = 0) -> int:
    df = carrega_dados(uri)

    return (df.physicians.iloc[index])


if __name__ == '__main__':

    uri = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'

    df = carrega_dados(uri)

    print(df.info())
