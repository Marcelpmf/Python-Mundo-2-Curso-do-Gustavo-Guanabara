numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2ª número: '))

opc = 0

while opc != 5:
    opc = int(input('\n[1] Somar\n'
                    '[2] Multiplicar\n'
                    '[3] Maior valor\n'
                    '[4] Novos números\n'
                    '[5] Sair do programa\n'))

    if opc == 1:
        print('A soma dos valores é: {}'.format(numero1+numero2))

    elif opc == 2:
        print('O produto dos valores é: {}'.format(numero1*numero2))

    elif opc == 3:
        if numero2 > numero1:
            print('O maior valor é {}'.format(numero2))
        elif numero1 > numero2:
            print('O maior valor é: {}'.format(numero1))
        else:
            print('Os dois valores são iguais')

    elif opc == 4:
        numero1 = int(input('Digite o NOVO 1º número: '))
        numero2 = int(input('Digite o NOVO 2ª número: '))

print('TERMINADO')

