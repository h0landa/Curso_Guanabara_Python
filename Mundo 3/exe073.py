tabela_brasileirao = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará SC', 'Corinthias', 'Coritiba', 'Cuiabá',
                      'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Chapecoense', 'Bragantino', 'Santos', 'São Paulo')
print(f'''Primeiros Colocados:{tabela_brasileirao[0:5]}
Ultimos 4 colocados:{tabela_brasileirao[-4:]}
Ordem alfabetica:{sorted(tabela_brasileirao)}''')
if 'Chapecoense' in tabela_brasileirao:
    print(
        f"Posição da Chapecoense na lista:{tabela_brasileirao.index('Chapecoense')}")
else:
    print('Chapecoense não está na lista')
