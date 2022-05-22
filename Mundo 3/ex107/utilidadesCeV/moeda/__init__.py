def metade(val, real=False):
    if real == True:
        return "R$ {:.2f}".format(val/2)
    else:
        return val/2


def dobro(val, real=False):
    if real == True:
        return "R$ {:.2f}".format(val * 2)
    else:
        return val * 2


def aumentar(val, porcentagem=0, real=False):
    if real == True:
        return "R$ {:.2f}".format(val + (val * porcentagem/100))
    if real == False:
        return val + (val * porcentagem/100)


def diminuir(val, porcentagem=0, real=False):
    if real == True:
        return "R$ {:.2f}".format(val - (val * porcentagem/100))
    else:
        return val - (val * porcentagem/100)

def moeda(val):
    return removerPonto("R$ {:.2f}".format(val))


def removerPonto(val):
    return str(val).replace('.',',')


def resumo(val, aumenta, diminui):
    resumo_dados = f"""Preço analisado: R$ {moeda(val)}
Dobro do preço: R$ {dobro(val, True)}
Metade do preço: R$ {metade(val, True)}
{aumenta}% de aumento: R$ {aumentar(val, aumenta, True)}
{diminui}% de redução: R$ {diminuir(val, diminui, True)}"""
    return removerPonto(resumo_dados)