from datetime import date


def voto():
    if idade >= 16 and idade <= 18:
        return "VOTO OPCIONAL"
    elif idade >= 18 and idade < 65:
        return "VOTO OBRIGATORIO"
    elif idade < 16:
        return "VOTO PROIBIDO"
    elif idade >= 65:
        return "VOTO OPCIONAL"


nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = str(date.today()).split("-")
idade = int(ano_atual[0]) - nascimento
print(f'Com {idade} anos: {voto()}')
