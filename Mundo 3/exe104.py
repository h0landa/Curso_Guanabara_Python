def leiaInt(var):
    ok = False
    valor = 0
    while True:
        n = str(input(var))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('ERRO. Digite um número inteiro valido.')
        if ok:
            break
        return valor
    
n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')