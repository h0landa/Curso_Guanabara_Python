def maior(lista):
    mai = 0
    for m in lista:
        if len(lista) == 0:
            mai = m
        else:
            if m > mai:
                mai = m
    print(f'Analisando os valores passados...')
    print(f'{lista} foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor foi {mai}.')

cont = 0
numeros = []
while True:
    num = int(input(f'COD[{cont}] - Digite um número:'))
    numeros.append(num)
    cont += 1
    quest = str(input('Quer continuar?: ')).upper()[0]
    if quest == 'N':
        break
    while quest != 'S':
        print('ERRO. Digite apenas "N" ou "S".')
        quest = str(input('Quer continuar?: ')).upper()[0]
maior(numeros)
