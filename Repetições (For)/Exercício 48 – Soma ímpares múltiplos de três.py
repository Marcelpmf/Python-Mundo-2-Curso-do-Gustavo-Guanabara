# pares: numero % 2 == 0 e impares: numero % 2 == 1

somador = 0
quantia = 0

for contador in range (1, 500):

    if contador % 2 == 1 and contador % 3 == 0:
        print(contador)
        somador += contador
        quantia += 1

print('A soma de todos os valores ímpares multiplos de 3 entre 1 ({} numeros) e 500 foi: \033[32m{}\033[m'
      .format(quantia, somador))



print('FIM')
