#Criar um algoritimo que leia um numero e mostre o seu dobro,triplo e raiz quadrada
num = int(input('Digite seu numero: '))

dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('Segue os resultados para o numero {}:\n Dobro:{}\n Triplo:{}\n Raiz Quadrada:{}'.format(num,dobro,triplo,raiz_quadrada))