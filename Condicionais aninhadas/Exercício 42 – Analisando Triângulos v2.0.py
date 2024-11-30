r1 = int(input('Digite o valor do 1º segmento de reta: '))
r2 = int(input('Digite o valor do 2º segmento de reta: '))
r3 = int(input('Digite o valor do 3º segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')

else:
    print('Não é triângulo')

#if r1 == r2 == r3  and  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #print('Triângulo Equilatero')

#elif r1 == r2 or r1 == r3 or r2 == r3  and  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #print('Triângulo Isosceles')

#elif r1 != r2 and r1 != r3 and r2 != r3  and  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #print('Triângulo Escaleno')

#else:
    #print('Não é triângulo')