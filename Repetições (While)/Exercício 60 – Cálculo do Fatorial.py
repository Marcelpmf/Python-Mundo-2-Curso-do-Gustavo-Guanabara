from math import factorial

numero = int(input('Digite um numero: '))
contador = numero
fatorial = factorial(numero)

print('Calculando {}! = '.format(numero), end='')

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1

print('{}'.format(fatorial))

