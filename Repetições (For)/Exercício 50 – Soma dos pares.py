somador = 0
quantia = 0

for contador in range (1, 7):
    
    numero = int(input('Digite o {}º número: '.format(contador)))

    if numero % 2 == 0:
        somador += numero
        quantia += 1

print('A soma dos {} numeros pares é: {}'.format(quantia, somador))

print('FIM')