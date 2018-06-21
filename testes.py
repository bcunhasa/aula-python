


# testes.py
import unittest
from nome import nome_formatado

class NomeTestsCase(unittest.TestCase):
    """Testes para a função nome_formatado"""
    
    def teste_primeiro_ultimo(self):
        """Checa se o nome 'Bruno Sá' executa"""
        nome = nome_formatado('bruno', 'sá')
        self.assertEqual(nome, 'Bruno Sá')

unittest.main()
