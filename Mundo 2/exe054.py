maior_de_idade = 0
menor_de_idade = 0
for c in range(0, 4):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    if 2022 - ano_nascimento > 18:
        maior_de_idade += 1
    elif 2022 - ano_nascimento < 18:
        menor_de_idade += 1
print('{} pessoas já são maior de idade\n{} pessoas ainda são menores de idade'.format(maior_de_idade, menor_de_idade))

