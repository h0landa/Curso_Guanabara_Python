def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f"O jogador {nome} fez {gols} gols no campeonato."
    

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Quantidade de gols: '))
print(ficha(nome,gols))