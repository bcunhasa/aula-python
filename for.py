


# Laços for e listas

nomes = ['alice', 'david', 'carolina']
for nome in nomes:
    print(nome)

# Criar lista de números
for valor in range(1, 5):
    print(valor)

numeros = list(range(1,6)); print(numeros)
numeros = list(range(2, 11, 2)); print(numeros)

quadrados = []
for valor in range(1, 11):
    quadrados.append(valor**2)
print(quadrados)

digitos = [7, 2, 3, 0, 8, 1]
print(min(digitos))
print(max(digitos))
print(sum(digitos))
