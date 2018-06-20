




# Instruções if

carros = ['audi', 'bmw', 'subaru', 'toytota']

for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

idade = 12

if idade < 4:
    preco = 0
elif idade < 15:
    preco = 5
elif idade < 65:
    preco = 10
else:
    preco = 5

print("O preço do ingresso custa R$ " + str(preco) + ".")
