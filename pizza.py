



# Pizza.py
def cria_pizza(tamanho, *ingredientes):
    """Mostra as informações de uma pizza"""
    print('Pizza de tamanho ' + str(tamanho) + 'cm')
    print('Ingredientes:')
    for ingrediente in ingredientes:
        print(ingrediente)
