def area(m, c):
    resultado = m * c
    print(f'A área do seu terreno é {resultado}m².')


print('CONTROLE DE TERRENOS')
metro = float(input('Quantos metro?: '))
comprimento = float(input('Qual comprimento?: '))
area(metro, comprimento)