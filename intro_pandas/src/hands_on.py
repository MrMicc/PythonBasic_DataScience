from urllib.parse import _NetlocResultMixinBase
import pandas as pd
from pandas.core.api import Series
from pandas.core.frame import Dtype


def carrega_dados(uri: str) -> pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=uri)  # type: ignore


def retorna_formato(ds: pd.DataFrame):

    return ds.shape


def tx_crime_no_indice(uri: str, index: int) -> float:

    df = carrega_dados(uri=uri)

    return (df.crime_rate.iloc[index])


def physicians_dado(uri: str, index: int = 0) -> int:
    df = carrega_dados(uri)

    return (df.physicians.iloc[index])


def new_label(uri: str, index, columns):
    df = carrega_dados(uri)

    return df.loc[index, columns]


def quantidade_de_regiao_igual_a(uri: str, valor: int = 2) -> int:

    df = carrega_dados(uri)

    # retorna total de regiões iguais ao valor
    return len(df[df.region == valor].index)  # type: ignore


if __name__ == '__main__':

    uri = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'

    df = carrega_dados(uri)

    print(df.info())

    print(new_label(uri, [1, 3, 5, 7, 9, 13], [
          'land_area', 'work_force', 'income', 'region', 'crime_rate']))
