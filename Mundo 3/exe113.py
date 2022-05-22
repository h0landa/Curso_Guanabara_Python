def leiaInt(var):
    while True:
        try:
            n = int(input(var))
        except(ValueError, TypeError):
            print('ERRO. Digite um número inteiro valido.')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu não digitar nenhum dado.')
            return 0
        else:
            return n


def leiaFloat(var):
    while True:
        try:
            n = float(input(var))
        except(ValueError, TypeError):
            print('ERRO. Digite um número real valido.')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu não digitar nenhum dado.')
            return 0
        else:
            return n
            
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {inteiro} e o número real {real}')