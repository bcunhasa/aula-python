


# escrita.py
nome_arquivo = 'dados.txt'

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write('Este é um exemplo')


with open(nome_arquivo, 'a') as arquivo:
    arquivo.write('Este é outro exemplo')
