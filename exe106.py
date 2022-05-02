def manual(var):
    print('=' * 30)
    print(f'INTERACTIVE HELP DE {var}')
    print('=' * 30)
    print(help(var))

name = str(input('Digite o comando: '))
manual(name)