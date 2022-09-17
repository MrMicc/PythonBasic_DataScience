from ..src.aula_01_ex_01 import soma


def test_soma():
    '''Valida soma de dois numeros inteiros'''

    recebi = soma(5,16)
    quero = 21

    assert recebi == quero

