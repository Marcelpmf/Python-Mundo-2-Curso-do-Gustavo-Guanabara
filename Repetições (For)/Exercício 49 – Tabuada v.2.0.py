numero = int(input('Digite o numero que você quer ver a tabuada: '))

# botar o in range ate numero + 10
# numero * contador (contador tem que começar com 1 ate 10)

print('Tabuada do {}'.format(numero))

for contador in range (1, 11):

    tabuada = contador * numero
    print ('{} x {} = {}'.format(numero, contador, tabuada))

print('FIM!')