



# Laços while
prompt = "\nDigite qualquer coisa e ela será repetida"
prompt += "\nDigite 'sair' para sair:"

mensagem = ''
while mensagem != 'sair':
    mensagem = input(prompt)
    print(mensagem)
