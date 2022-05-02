from datetime import date


dados_trabalhistas = []
trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = str(input('Data de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho[1/0]: '))
if trabalhador['ctps'] == 1:
    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: '))
    dados_trabalhistas.append(trabalhador)
    ano_nascimento = trabalhador['nascimento']
    ano_nascimento = ano_nascimento.split('/')
    ano_nascimento = int(ano_nascimento[2])
    data_atual = date.today()
    idade = trabalhador['ano_contratacao'] - ano_nascimento
    print(f'Você ira se aposentar em {trabalhador["ano_contratacao"] + 35} com {idade + 35} anos')
print(dados_trabalhistas)