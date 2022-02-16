#calcular preço a pagar sabendo que o carro custa 60 reais por dia e 0,15 por km rodado.
km = int(input('Quantos kilometros rodados?: '))
dias = int(input('Quantos dias?: '))

print('Sua conta ficou R${:.2f}'.format(km*0.15+dias*60))