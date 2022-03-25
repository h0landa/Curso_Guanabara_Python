palavras = ('casa', 'onibus', 'caminhao', 'pente', 'computador')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for letra in p:
        if letra in vogais:
            print(letra, end='')
