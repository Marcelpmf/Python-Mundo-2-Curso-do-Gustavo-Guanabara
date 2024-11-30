somador = maiorquemil = contador = menor = 0
barato = ' '

while True:

    nome = str(input('\nNome do produto: '))

    valor = float(input('Preço: R$'))
    somador += valor
    contador += 1

    if valor > 1000:
        maiorquemil += 1

    if contador == 1 or valor < menor:
        menor = valor
        barato = nome

    #else: PODE SER ASSIM TB
        #if valor < menor:
            #menor = barato
            #barato = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'O total da compra foi \033[33mR${somador:.2f}\033[m'
      f'\nTemos \033[33m{maiorquemil}\033[m produtos custando mais de R$1000'
      f'\nO produto mais barato é o \033[33m{barato}\033[m')


