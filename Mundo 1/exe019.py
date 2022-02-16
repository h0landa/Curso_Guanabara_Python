#Programa para ler o nome de quatro alunos e sortear o nome de um.

import random

name1 = input('Digite um nome: ')

name2 = input('Digite um nome: ')

name3 = input('Digite um nome: ')

name4 = input('Digite um nome: ')

lista_nomes = [name1,name2, name3, name4]
sorteado = random.choice(lista_nomes)

print('O aluno sorteado foi: {}'.format(sorteado))