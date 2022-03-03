primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão'))
decimo_termo = primeiro_termo +  (10 - 1) * razao
c = primeiro_termo - razao
while c <= decimo_termo:
    c += razao
    print('{}->'.format(c), end='')
print('FIM')
    