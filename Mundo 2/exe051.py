primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo, razao):
    print('{} '.format(c), end='-> ')
print('Acabou')
