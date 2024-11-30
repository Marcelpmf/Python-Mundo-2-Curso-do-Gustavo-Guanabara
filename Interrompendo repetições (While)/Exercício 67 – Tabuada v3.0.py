while True:

    print('='*33)
    numero = int(input('Quer ver a tabuada de qual valor: '))

    print('=' * 33)
    if numero < 0:
        break
    for contador in range (1,11):
        tabuada = numero * contador
        print(f'{numero} x {contador} = {tabuada}')


print('FIM')

