



# cachorro.py
class Cachorro():
    """Uma classe que representa um cachorro"""
    
    def __init__(self, nome, idade):
        """Inicializa as variáveis da classe"""
        self.nome = nome
        self.idade = idade
    
    def senta(self):
        """Faz o cachorro sentar"""
        print("O cachorro sentou")
    
    def late(self):
        print("O " + self.nome + " sentou")
    
    def get_idade(self):
        return str(self.idade)

cachorro1 = Cachorro('júlio', 5)
print(cachorro1.nome)
print(cachorro1.get_idade())
cachorro1.nome = 'marcos'
print(cachorro1.nome)
