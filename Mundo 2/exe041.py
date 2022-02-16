import datetime

ano_nascimento = int(input('Digite seu ano de nascimento: '))

date = datetime.date.today()
year = date.strftime('%Y')
year = int(year)
idade = year - ano_nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')