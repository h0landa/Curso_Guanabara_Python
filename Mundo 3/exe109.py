from ex107.utilidadesCeV.moeda import resumo, aumentar, diminuir, dobro, metade, moeda

valor = float(input('Digite um valor: '))
print(f'''A metade de {moeda(valor)} é {metade(valor)}
O dobro de {moeda(valor)} é {dobro(valor, True)}
Aumentando 10% de {moeda(valor)} temos {aumentar(valor, 10, False)}
Diminuindo 13% de {moeda(valor)} temos {diminuir(valor, 13, True)}''')