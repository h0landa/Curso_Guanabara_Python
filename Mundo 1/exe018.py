#Programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print('Para o angulo {}°, temos os seguintes resultados: cosseno={:.3f}, seno={:.3f}, tangente={:.3f}.'.format(angulo, cosseno, seno, tangente))