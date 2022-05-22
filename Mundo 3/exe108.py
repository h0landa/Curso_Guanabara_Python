from ex107.utilidadesCeV import moeda

valor = float(input('Digite um valor: '))
print(f'''A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}
O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}
Aumentando 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.aumentar(valor, 10))}
Diminuindo 13% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.diminuir(valor, 13))}''')