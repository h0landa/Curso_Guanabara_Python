from posixpath import split
from random import choice

minha_escolha = str(input('Digite sua escolha: '))

escolhas_pc = 'Pedra Papel Tesoura'
escolhas_pc = escolhas_pc.split()
escolhas_pc = choice(escolhas_pc)

if minha_escolha == 'Tesousa' and escolhas_pc == 'Papel':
    print('Você me venceu!')
elif minha_escolha == 'Papel' and escolhas_pc == 'Pedra':
    print('Você me venceu!')
elif minha_escolha == 'Pedra' and escolhas_pc == 'Tesoura':
    print('Você venceu!')
elif minha_escolha == escolhas_pc:
    print('EMPATE')
else:   
    print('Você foi derrotado!')
print(25 * '+=')
print('Sua escolha:{}\nEscolha do computador:{}'.format(minha_escolha, escolhas_pc))
print(25 * '+=')
