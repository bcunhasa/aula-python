



# leitura.py
with open('dados.txt') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('dados.txt') as arquivo:
    for linha in arquivo:
        print(linha)

