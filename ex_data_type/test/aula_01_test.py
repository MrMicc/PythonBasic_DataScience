from ..src.aula_01 import soma, cubo, subtrai_total_duas_listas

from unittest import TestCase 
from unittest.mock import patch 

def test_soma():
    '''Valida soma de dois numeros inteiros'''

    recebi = soma(5,16)
    quero = 21

    assert recebi == quero


class TestCubo(TestCase):
    
    @patch('builtins.input', return_value='3')
    def test_cubo(self, return_mock):
        '''Valida e faz mock de calculo ao cubo de um numero inteiro''' 

        recebi = cubo()
        quero = 27

        assert recebi == quero



def test_subtrai_total_duas_listas():
    '''Valida a soma de duas listas inteiras''' 

    l1 = [10, 20, 30, 25, 32, 45, 50]
    l2 = [80, 70, 78, 55, 62]
    
    recebi = subtrai_total_duas_listas(l1, l2)
    quero = -133 

    assert quero == recebi 

