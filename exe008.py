#CONVERSOR DE METROS PARA CENTIMETROS
metros = int(input('Digite os metros: '))
metros_para_centimetros = metros * 100
metros_para_milimetros = metros * 1000

print('''Aqui estão os resultados de {} metros convertidos:\n
{} Metros em centimetros:{}\n 
{} Metros em milimetros:{}'''
.format(metros,metros,metros_para_centimetros,metros,metros_para_milimetros))
