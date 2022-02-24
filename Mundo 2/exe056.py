quantidade_mulheres = 0
media_idade = 0
nome_homem_mais_velho = ''
maior_idade_homem = 0
somaidade = 0
for c in range(1,5):
    print('----- {}° Pessoa -----'.format(c))
    nome = str(input('Digite o {}° nome: '.format(c)))
    idade = int(input('Digite a {}° idade: '.format(c)))
    sexo = str(input('Digite seu sexo[M\F]: '.format(c)))
    somaidade = somaidade + idade
    if sexo == 'F' and idade < 20:
        quantidade_mulheres += 1
    if sexo == 'M' and c == 1:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
media_idade = somaidade/4
print('A media da idade do grupo é igual a:{}'.format(somaidade))
print('O homem mais velho tem {} anos e seu nome é:{}'.format(maior_idade_homem, nome_homem_mais_velho))
print('A quantidade de mulheres com menos de 20 anos é:{}'.format(quantidade_mulheres))
    


    
