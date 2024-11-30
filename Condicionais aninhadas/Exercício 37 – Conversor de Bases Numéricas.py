numero = int(input('Digite um número inteiro: '))

escolha = int(input('\nDigite qual base de conversão: '
                    '\n[  1  ] Binário'
                    '\n[  2  ] Octal'
                    '\n[  3  ] Hexadecimal'
                    '\nDigite: '))

if escolha == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero) [2:]))

elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))

elif escolha == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))

else:
    print('Opção inválida, tente novamente.')




