numero = somador = quantidade = 0

# numero = int(input('Digite um número: [999 pra parar]'))
while numero != 999:

    numero = int(input('Digite um número: '))

    if numero != 999:                   # TEM COMO TIRAR ESSE IF
        quantidade += 1
        somador += numero

    # somador += numero
    # contador += 1
    # numero = int(input('Digite um número: [999 pra parar]'))

print('Soma dos {} números digitados = {}'.format(quantidade, somador))

