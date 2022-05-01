lista = []
for c in range(0, 4):
    num = int(input(f'Digite o {c}ª número: '))
    while num in lista:
        print(f'O número {num} já está na lista.')
        num = int(input('Digite novamente: '))
    lista.append(num)
print(f'Todos os valores {sorted(lista)}')
    