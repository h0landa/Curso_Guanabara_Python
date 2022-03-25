num = int(input('Quanto você quer sacar ?: '))
quant_unid = quant_dez = quant_cent = quant_vinte = quant_cinquenta = 0
c = 0
for c in range(0, num + 1):
    if c == 100:
        quant_cent += 1
    if c == 50:
        quant_cinquenta += 1
    elif c == 20:
        quant_vinte += 1        
    elif c == 10:
        quant_dez += 1
    elif c == 1:
        quant_unid += 1
print(f'''Quantidade notas de 100:{quant_cent}''')
print(f'''Quantidade notas de 50:{quant_cinquenta}''')
print(f'''Quantidade notas de 20:{quant_vinte}''')
print(f'''Quantidade notas de 10:{quant_dez}''')
print(f'''Quantidade notas de 1:{quant_unid}''')
    
            
#print(f'''Quantidade notas de 50:{quant_cinquenta}
#Quantidade notas de 20:{quant_vinte}''')