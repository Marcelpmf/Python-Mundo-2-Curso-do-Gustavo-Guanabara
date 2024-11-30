resposta = ''

media = somador = quantidade = maior = menor = 0

while resposta != 'N': # while resposta in 'S' TEM COMO FAZER ASSIM TB

    numero = int(input('Digite um número: '))
    somador += numero
    quantidade += 1
    media = somador / quantidade


    if quantidade == 1: # pra poder comparar os numeros tem que ser a partir do primeiro numero digitado
        maior = numero
        menor = numero

    else:

        if numero > maior:
            maior = numero

        elif numero < menor:
            menor = numero

    resposta = str(input('Você quer continuar? [S/N] ')).upper()


print('\nForam digitados \033[33m{}\033[m numeros.\n'
      'O maior valor foi: \033[33m{}\033[m\n'
      'O menor valor foi: \033[33m{}\033[m\n'
      'A média foi: \033[33m{:.2f}\033[m\n'.format(quantidade, maior, menor, media))