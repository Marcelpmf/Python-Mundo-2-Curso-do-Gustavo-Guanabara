n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('Primeiro valor maior ({} > {}).'.format(n1, n2))
elif n2 > n1:
    print('Segundo valor maior ({} > {}).'.format(n2, n1))
else:
    print('Os dois valores são iguais.({} = {})'.format(n1, n2))