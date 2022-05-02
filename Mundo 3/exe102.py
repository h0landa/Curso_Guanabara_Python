def fatorial(num, show=False):
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        print(f)
    if show == True:
        for c in range(num, 0, -1):
            f *= c
        
        for c in range(num, 0, -1):
            print(f'{c}', end=' x ')
            if c == 2:
                print(1, end=' ')
                break
        print('=', f)
num = int(input('Digite um número para fatora-lo: '))
conta = str(input('Quer ver a conta ?: ')).upper()[0]
if conta == 'S':
    fatorial(num, show=True)
elif conta == 'N':
    fatorial(num)
else:
    while conta != 'N' and conta != 'S':
        print("ERRO. Digite apenas 'S' ou 'N'.")
        conta = str(input('Quer ver a conta ?: '))
        