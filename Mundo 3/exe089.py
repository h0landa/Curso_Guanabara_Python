#todos_alunos[nomes[notas]]
#todos_alunos.append(nomes)
quest = 'S'
todos_alunos = []
while not 'N' in quest:
    nota = []
    nome = []
    nome_aluno = str(input('Digite o nome do aluno: '))
    nome.append(nome_aluno)
    for cont in range(0, 2):
        nota_aluno = float(input(f'Digite a {cont}ª nota: '))
        nota.append(nota_aluno)
    quest = str(input('Quer continuar ?[S/N]: '))
    alunos = [nome,nota]
    todos_alunos.append(alunos[:])
print(f'No.     Nomes     Media')
cod_aluno = 0
for dados in todos_alunos:
    print(cod_aluno,end='     ')
    print(dados[0][0],end='     ')
    print(sum(dados[1]) / 2)
    cod_aluno += 1
mostrar_nota = 0
while not 999 in mostrar_nota:
    mostrar_nota = int(input('Mostrar notas de qual aluno?: '))
    print(f' As notas de {todos_alunos[mostrar_nota][0][0]} são {todos_alunos[mostrar_nota][1]}')