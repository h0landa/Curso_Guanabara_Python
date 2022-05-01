jogadores = []
jogador = {}
gols = []
cod = 0
while True:
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do jogador: '))

    quant_partidas = int(input('Quantas partidas ?: '))
    for g in range(0, quant_partidas):
        quant_gols = int(input(f'Quantidade de gols na {g}ª partida: '))
        gols.append(quant_gols)
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    cod += 1

    cont = str(input('Quer continuar ?: ')).strip().upper()
    if cont == 'N':
        break
for dados in jogadores:
    print(dados)
while True:
    escolha_jogador = int(input('Digite o código do jogador para mostrar seus dados: '))
    if escolha_jogador < 0:
        break
    for dados in jogadores:
        if escolha_jogador == dados['cod']:
            print(f'*** Levantamento do Jogador {dados["nome"]} ***')
            for d in range(0, len(dados['gols'])):
                print(f'No jogo {d} fez {dados["gols"][d]} gols')

