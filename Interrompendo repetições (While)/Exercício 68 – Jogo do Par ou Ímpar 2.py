from random import randint
vitoria = 0 # ou contador

while True:
    jogador = int(input('Diga um numero de 0 a 10: '))
    computador = randint(0, 10)

    soma = jogador + computador

    par_impar = ' '

    while par_impar not in 'PI':
        par_impar = str(input('Par ou Impar? ')).strip().upper()[0] # primeira letra e dividido
    print(f'você jogou {jogador} e o computador jogou {computador}. Total de {soma}', end='')

    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')

    if par_impar == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('VOCÊ PERDEU :(')
            break

    elif par_impar == 'I':
        if soma % 2 == 1:
            print('VOÊ VENCEU')
            vitoria += 1
        else:
            print('VOCÊ PERDEU :(')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! você venceu {vitoria} vezes')



