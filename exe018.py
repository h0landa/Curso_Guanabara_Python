#Programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite um ângulo: '))

seno = math.sin(angulo)

cosseno = math.cos(angulo)

tangente = math.tan(angulo)

print('Para o angulo {}°, temos os seguintes resultados: cosseno={:.3f}, seno={:.3f}, tangente={:.3f}.'.format(angulo, cosseno, seno, tangente))