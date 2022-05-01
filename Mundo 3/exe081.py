lista = []
c = cinco_true = 0
while True:
    num = int(input(f'Digite o {c}ª número: ' ))
    if num < 0:
        break
    lista.append(num)
    c += 1
lista = sorted(lista, reverse=True)
if 5 in lista:
    cinco_true = 'O valor 5 está na lista'
else:
    cinco_true = 'O valor 5 não está na lista'
print(f'''Foram digitados {len(lista)} números
Lista em ordem decrescente: {lista}
{cinco_true} na posição {lista.index(5)}''')
print(len(lista))
