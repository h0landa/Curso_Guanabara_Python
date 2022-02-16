# O programa deve ler o nome de uma pessoa e mostrar ele com todas as letras minusculas,
#com todas letras maiusculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome.

nome = 'Arthur da Costa Holanda'

maiusculas = nome.upper()

minusculas = nome.lower()

quantidade = nome.replace(" ","")

quantidade_no_space = len(quantidade)

quantidade_primeiro_nome = nome.split()

print('''Para o nome {}, temos os seguintes textos:\n Maiúsculas: {} \n Minusculas:{} 
\n Quantidade de letras:{} \n Quantidade de letras no primeiro nome: {} '''.format(nome, maiusculas, minusculas, quantidade_no_space,len(quantidade_primeiro_nome[0])))