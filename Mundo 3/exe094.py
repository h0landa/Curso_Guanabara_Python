pessoas = []
pessoa = {}
mulheres = []
acima_da_media = []
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo: ')).strip().upper()
    if pessoa['sexo'] != 'M' or pessoa['sexo'] != 'F':
        while True:
            print('ERRO. Digite apenas "M" ou "F".')
            pessoa['sexo'] = str(input('Sexo: ')).strip().upper()
            if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
                break 
    pessoas.append(pessoa.copy())
    quest = str(input('Quer continuar ?[S/N]: ')).strip().upper()
    if quest == 'N':
        break
    else:
        while quest != 'S':
            print('ERRO. Digite apenas "S" ou "N".')
            quest = str(input('Quer continuar ?[S/N]: ')).strip().upper()
print(f'Foram cadastradas {len(pessoas)} pessoas.')

for m in pessoas:
    soma += m['idade']
    if m['sexo'] == 'F':
        mulheres.append(m['nome'])
    media = soma/len(pessoas)
    if m['idade'] > media:
        acima_da_media.append(m['nome'])
print(f'Pessoas com idade acima da media: {acima_da_media}')
print(f'A media de idade do grupo é {media}')
print(f'Todas as mulheres: {mulheres}')

