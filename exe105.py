def notas(* num):
    """A função retorna:
    -> Maior nota;
    -> Menor nota;
    -> Media da turma;"""
    mai = men = soma = media = 0
    for n in num:
        soma += n
        if len(num) == 0:
            mai = n 
            men = n
        else:
            if n < men:
                men = n
            if n > mai:
                mai = n
            
    media = soma/len(num)
    return f'''Quantidade de notas: {len(num)}
    Maior nota: {max(num)}
    Menor nota: {min(num)}
    Media da turma: {media}'''
print(notas(5, 6, 7, 1, 3, 10))
tupla = (5, 5, 6, 8, 1)