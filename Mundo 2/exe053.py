frase = str(input('Digite uma frase: '))
frase.replace(" ","")
quantidade_letras = len(frase)

if frase == frase[::-1]:
    print('A frase "{}" é um palindromo.'.format(frase))
else:
    print('A frase "{}" não é um palindromo'.format(frase))