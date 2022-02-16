'''Programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa.'''

import math

co = float(input('Digite o cateto oposto: '))

ca = float(input('Digite o cateto adjascente: '))

quadrado_dos_cateos = math.pow(co,2) + math.pow(ca,2)

hipotenusa = math.sqrt(quadrado_dos_cateos)

print('O valor da hipotenusa é: {}'.format(hipotenusa))