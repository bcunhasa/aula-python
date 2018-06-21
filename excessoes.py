


# excessoes.py
try:
    print(4/0)
except ZeroDivisionError:
    print("Você não pode dividir por zero")

nome_arquivo = 'algumacoisa.txt'

try:
    with open(nome_arquivo) as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não existe")
        
