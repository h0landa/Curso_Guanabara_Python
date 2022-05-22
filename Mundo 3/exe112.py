from ex107.utilidadesCeV.dado import leiaDinheiro
from ex107.utilidadesCeV.moeda import resumo


n = leiaDinheiro('Digite o preço: R$')
print(resumo(n, 10, 25))