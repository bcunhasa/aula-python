


# heranca.py
class Carro():
    """Classe que representa um carro"""
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def descricao(self):
        return self.marca + ', ' + str(self.ano)


class CarroEletrico(Carro):
    """Classe que representa um carro elétrico"""
    def __init__(self, marca, ano, consumo):
        super().__init__(marca, ano)
        self.consumo = consumo
    
    def mostra_consumo(self):
        return 'Cosumo: ' + str(self.consumo)
    
    def descricao(self):
        return 'Este método foi alterado'
