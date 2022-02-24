l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Esses lados formam um triângulo ', end='')
    if l1 == l2 and l2 == l3:
        print('EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISOSCELES') 
else:
    print('Esses lados não formam um triângulo.')