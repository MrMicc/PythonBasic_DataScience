import pandas as pd


def carrega_dados(uri: str, sep=',') -> pd.Series:
    return pd.read_csv(uri, sep=sep)


def retorna_formato(ds: pd.Series):

    return ds.shape


def tx_crime_no_indice(uri: str, index: int) -> float:

    df = carrega_dados(uri=uri)

    return df.loc[index, ['crime_rate']]


if __name__ == '__main__':

    uri = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'

    df = carrega_dados(uri)

    print(df.info())

    print(tx_crime_no_indice(uri=uri, index=9))
