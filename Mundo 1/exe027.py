# Fazer programa leia o nome de uma pessoa e mostra seu primeiro e seu ultimo nome.

nome = 'Arthur da Costa Holanda'

nome = nome.split()

primeiro_nome = nome[0]

quantidade_palavras = len(nome)

ultimo_nome = nome[quantidade_palavras -1]

print('Primeiro nome: ',primeiro_nome)
print('Ultimo nome: ',ultimo_nome)