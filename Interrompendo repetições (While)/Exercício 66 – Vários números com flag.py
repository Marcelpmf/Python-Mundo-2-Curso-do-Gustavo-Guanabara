numero = contador = somador = 0

while True:


    numero = int(input('Digite um número (999 para parar: '))

    if numero == 999:
        break

    contador += 1
    somador += numero

print(f'Foram digitados \033[32m{contador}\033[m números e a soma entre eles foi \033[32m{somador}\033[m')
