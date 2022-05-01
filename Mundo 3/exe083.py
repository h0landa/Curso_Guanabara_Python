expressao = []
linha = str(input('Digite sua expressão: '))
for c in range(0, len(linha)):
    expressao.append(linha[c])
quant_parenteses_dir = expressao.count('(')
quant_parenteses_esque = expressao.count(')')
if quant_parenteses_dir != quant_parenteses_esque:
    print('Sua expressão está incorreta')
else:
    print('Sua expressão está correta')
