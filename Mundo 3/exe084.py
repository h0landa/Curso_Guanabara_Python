pessoas = []
quest = 'S'
mais_pesada = mais_leve = c = 0
while not 'N' in quest:
    dados = []
    nome = str(input('Digite um nome: '))
    peso = float(input('Digite um peso: '))
    dados.append(nome)
    dados.append(peso)
    if len(pessoas) == 0:
        mais_pesada = mais_leve = dados[1]
    else:
        if dados[1] > mais_pesada:
            mais_pesada = dados[1]
        if dados[1] < mais_leve:
            mais_leve = dados[1]
    pessoas.append(dados[:])
    quest = str(input('Quer continuar ?: ')).strip().upper()
    c += 1
print(f'O maior peso foi de: {mais_pesada}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == mais_pesada:
        print(f'{p[0]}')
print(f'O menor peso foi de: {mais_leve}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == mais_leve:
        print(f'{p[0]}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
