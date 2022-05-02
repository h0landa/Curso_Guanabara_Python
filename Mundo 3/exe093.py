gols = []
jogador = {'gols': gols}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['quant_partidas'] = int(input('Quantas partidas?: '))
for q in range(0, jogador['quant_partidas']):
    quant_gols = int(input(f'Quantidade de gols na {q}ª partida: '))
    gols.append(quant_gols)

print(f'''Jogador: {jogador["nome"]}
Total Gols: {sum(jogador["gols"])}
Todos os Gols: {jogador["gols"]}''')
print(f'''### O jogador {jogador["nome"]} jogou {jogador["quant_partidas"]} partidas ###''')

c = 0
for p in jogador['gols']:
    print(f'Na partida {c}, fez {p} gols.')
    c += 1