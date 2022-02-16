#Mostrar salario com 15% de aumento

salario = float(input('Qual o valor do salario?: '))

aumento = 15/100

valor_com_aumento = salario + (salario * aumento)

print('O valor do seu produto é:R${:.2f} e com aumento fica por:R${:.2f}'.format(salario,valor_com_aumento))