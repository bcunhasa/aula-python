



# Funções

def saudacao(nome):
    """Escreve uma saudação ao usuário"""
    print("Olá " + nome + ".")

saudacao('Bruno')    

# Argumentos opcionais
def nome_formatado(primeiro_nome, segundo_nome=''):
    """Retorna o nome completo formatado"""
    return primeiro_nome.title() + segundo_nome.title()

nome = nome_formatado('bruno ', 'de sá')
print(nome)

nome = nome_formatado('bruno')
print(nome)

# Argumentos nomeados
def descreve_animal(nome, tipo):
    """Mostra as informações de um animal"""
    print('Nome: ' + nome)
    print('Tipo: ' + tipo)

descreve_animal(nome='Neymar', tipo='Capivara')
descreve_animal(tipo='Capivara', nome='Neymar')

print('\n\n')
# Valores default
def descreve_animal(nome, tipo='Cachorro'):
    """Mostra as informações de um animal"""
    print('Nome: ' + nome)
    print('Tipo: ' + tipo)

descreve_animal(nome='Neymar', tipo='Capivara')
descreve_animal(nome='Neymar')

print('\n\n')
# Número arbitrário de argumentos
def pizza(tamanho, *ingredientes):
    """Mostra as informações de uma pizza"""
    print('Pizza de tamanho ' + str(tamanho) + 'cm')
    print('Ingredientes:')
    for ingrediente in ingredientes:
        print(ingrediente)

pizza(20, 'ingrediente1', 'ingrediente2', 'ingrediente3')
