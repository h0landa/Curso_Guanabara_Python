def escreva(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

print('SUA MENSAGEM')
mensagem = str(input('Digite sua mensagem: '))
escreva(mensagem)