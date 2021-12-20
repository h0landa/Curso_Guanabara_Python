#O programa deve ler a altura e largura de uma parede em metros e calcular sua área e a quantidade de tinta necessaria para pinta-la.

altura = int(input('Digite a altura da parede(Metros)'))

largura = int(input('Digite a largura da parede(Metros)'))

area = altura * largura

quantidade_de_tinta = area/2

print('A quantidade de tinta necessaria para pintar sua parede é de:{} litros'.format(quantidade_de_tinta))