#Ler nome de 4 alunos e mostrar na tela em ordem sorteada.

from random import shuffle

name1 = input('Digite um nome: ')

name2 = input('Digite um nome: ')

name3 = input('Digite um nome: ')

name4 = input('Digite um nome: ')

lista_nomes = [name1,name2, name3, name4]

sorteado = shuffle(lista_nomes)

print('O aluno sorteado foi: {}'.format(lista_nomes))