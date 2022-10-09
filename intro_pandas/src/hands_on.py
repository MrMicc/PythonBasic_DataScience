import pandas as pd


def carrega_dados(uri: str, sep = ',') -> pd.Series:
    return pd.read_csv(uri, sep=sep)




def retorna_formato(ds: pd.Series):

    return ds.shape



if __name__ == '__main__':
    
    uri = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'

    df = carrega_dados(uri)

    print(retorna_formato(df))


    print(df.info())
