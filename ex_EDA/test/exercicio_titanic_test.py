from src.exercicio_titanic import carrega_data_set, quantidade_de_dados_nulos, quantidade_de_passageiros_por_genero



DADOS = carrega_data_set()



def test_quantidade_de_dados_nulos():

    recebi = quantidade_de_dados_nulos(DADOS,coluna='Fare')
    quero = 0

    assert recebi == quero



def test_quantidade_de_passageiros_por_genero():
    recebi = quantidade_de_passageiros_por_genero(DADOS)
    quero = {'f':314, 'm':577}
    
    print(recebi)
    assert quero == recebi
