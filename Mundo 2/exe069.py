mais_de_dezoito = homens_cadastrados = mulheres_menos_20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).upper()
    escolha = str(input('Quer continuar[S/N]: ')).upper()
    if escolha == 'N':
        break
    if idade >= 18:
        mais_de_dezoito += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
print('Programa encerrado')
print(f'''
Quantidade de pessoas com mais de 18:{mais_de_dezoito}
Quantidade de homens cadastrados:{homens_cadastrados}
Quantidade de mulheres com menos de 20 anos:{mulheres_menos_20}''')
