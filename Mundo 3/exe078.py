lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite {c}ª valor: ')))
maior_valor = max(lista)
menor_valor = min(lista)
print(f'''Maior valor {maior_valor} na posição {lista.index(maior_valor)} 
Menor valor {min(lista)} na posição {lista.index(menor_valor)}''')
