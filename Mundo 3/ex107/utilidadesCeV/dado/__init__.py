def leiaDinheiro(val):
    valido = False
    while not valido:
        entrada = str(input(val)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print('ERRO. Digite um número inteiro valido.')
        else:
            valido = True
            return float(entrada)