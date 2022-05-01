aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))

print(f'Nome do aluno: {aluno["nome"]}')
print(f'Media do aluno: {aluno["media"]}')
if aluno['media'] < 7:
    print('Situação do aluno: Reprovado')
else:
    print('Situação do aluno: Aprovado')