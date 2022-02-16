import datetime
from unittest import result

date = datetime.date.today()
year = date.strftime('%Y')
year = int(year)

ano_nascimento = int(input('Digite seu ano de nascimento: '))

resultado = year - ano_nascimento

if resultado == 18:
    print('Já está na hora de se alistar.')
elif resultado < 18:
    print('Ainda faltam {} ano para você se alistar.'.format(18 - resultado))
else:
    print('Você devia ter se alistado {} ano atrás.'.format(resultado - 18))