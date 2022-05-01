series = {}
netflix = []
for c in range(0,3):
    series['nome'] = str(input('Nome da serie: '))
    series['Temp'] = int(input('Quant. Temporadas: '))
    series['PersPrinc'] = str(input('Pers. Principal: '))
    netflix.append(series.copy())
for s in netflix:
    print(f'''Nome da serie: {s['nome']}
    Quant. Temporadas: {s['Temp']}
    Pers. Principal: {s['PersPrinc']}''')
