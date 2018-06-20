


# Dicionários
alien = {
    'cor'   : 'verde',
    'pontos': 5
}

print(alien)
print(alien['pontos'])

# Adicionar novo par chave-valor
alien['posicao_x'] = 0
alien['posicao_y'] = 25
print(alien)

# Dicionário vazio
novo_alien = {}
novo_alien['cor'] = 'azul'
print(novo_alien)

# Alterar valor
novo_alien['cor'] = 'amarelo'
print(novo_alien)

# Remover um valor
del novo_alien['cor']
print(novo_alien)

# Percorrer dicionários
linguagens = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for chave, valor in linguagens.items():
    print("Chave: " + chave)
    print("Valor: " + valor)

for nome in linguagens.keys():
    print(nome.title())

print('\n')

for linguagem in linguagens.values():
    print(linguagem)
