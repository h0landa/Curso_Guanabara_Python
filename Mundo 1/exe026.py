# O programa deve ler uma frase e identificar quantas vezes aparece a letra 'A', em que posição
# ela aparece na primeira vez e em que posição ela aparece na ultima.

frase = str(input('Digite uma frase: ')).upper().strip()

vezes_a = frase.count('A')

posicao_a = frase.find('A') + 1

ultima_posicao_a = frase.rfind('A') + 1

print('Quantas vezes aparece:{} \nQue posição começa:{} \nQue posição termina:{}'.format(vezes_a, posicao_a, ultima_posicao_a))