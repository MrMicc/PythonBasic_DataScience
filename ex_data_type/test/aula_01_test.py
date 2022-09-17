from ..src.aula_01 import soma, cubo

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


