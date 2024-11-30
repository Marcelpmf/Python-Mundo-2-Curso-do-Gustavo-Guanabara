from random import randint
contador = numero = vitorias = 0

while True:

    numeroPC = randint(1, 10)
    print(numeroPC)

    print('='*20)
    print('Jogo do Par ou Impar')
    print('='*20)

    numero = int(input('Digite um valor: '))
    par_imp = str(input('Par ou ímpar? [P/I]')).upper()
    soma = numero + numeroPC

    if par_imp == 'P':
        par_impPC = 'I'
    else:
        par_impPC = 'P'

    if soma % 2 == 0:
        print('-' * 20)
        print(f'Você jogou {numero} e o PC jogou {numeroPC}. O total foi {soma} e DEU PAR')
        print('-' * 20)

    else:
        print('-' * 20)
        print(f'Você jogou {numero} e o PC jogou {numeroPC}. O total foi {soma} e DEU ÍMPAR')
        print('-' * 20)

    if soma % 2 == 0 and par_imp == 'P' and par_impPC == 'I':
        print('VOCÊ VENCEU!')
        contador += 1

    elif soma % 2 == 0 and par_imp == 'I' and par_impPC == 'P':
        print('VOCÊ PERDEU!')
        break

    elif soma % 2 == 1 and par_imp == 'I' and par_impPC == 'P':
        print('VOCÊ VENCEU!')
        contador += 1

    elif soma % 2 == 1 and par_imp == 'P' and par_impPC == 'I':
        print('VOCÊ PERDEU!')
        break

print('='*20)

if contador > 0:
    print(f'GAME OVER. você ganhou {contador} vezes')


