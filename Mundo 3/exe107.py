from ex107 import moeda


valor = float(input('Digite um valor: '))
print(f'''A metade de {valor} é {moeda.metade(valor)}
O dobro de {valor} é {moeda.dobro(valor)}
Aumentando 10% de {valor} temos {moeda.aumentar(valor, 10)}
Diminuindo 13% de {valor} temos {moeda.diminuir(valor, 13)}''')