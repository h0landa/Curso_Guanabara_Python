# O programa deve ler o nome de uma pessoa e dizer se tem silva nele.

nome = input('Digite seu nome: ')

silva = 'SILVA' in nome.upper()

print('O nome {} tem "Silva" ? '.format(nome))
print(silva)