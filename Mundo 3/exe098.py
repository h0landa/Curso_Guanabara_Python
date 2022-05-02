def contador():
    c = 0
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(0, 10 + 1):
        print(c)
    print('Contagem de 10 até 0 de 2 em 2:')
    for x in range(10, -2, -2):
        print(x)


def personalizada(begin, end, step):
    c = 0
    print(f'Contagem de {begin} até {end} de {step} em {step}:')
    for c in range(begin, end + 1, step):
        print(c)


contador()

print('Agora faça sua contagem personalizada:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
personalizada(inicio, fim, passo)
