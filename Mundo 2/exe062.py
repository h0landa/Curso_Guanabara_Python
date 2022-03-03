primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
exit = False
for c in range(primeiro_termo, decimo_termo + 1, razao):
    print(c)
while not exit:
    quantidade_termos = int(input('Quantos termos você quer mostrar a mais?: '))
    decimo_termo = c + (quantidade_termos - 1) * razao
    for c in range(c, decimo_termo + 1, razao):
        print(c)
    if primeiro_termo == 0:
        print('Programa encerrado')
        exit = True

