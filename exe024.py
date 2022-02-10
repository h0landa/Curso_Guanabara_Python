# O programa deve ler o nome de uma cidade e identificar se começa com santo.

cidade = input('Digite o nome da cidade: ')

cidade_s = cidade.split()
cidade_s = 'santo' in cidade_s[0].lower()

print('A cidade {} possui "Santo" no nome? = '.format(cidade))
print(cidade_s)