from random import randint

numeroA = randint(0,10)
numero = 0
quantidade = 0

print(numeroA)

while numero != numeroA:

    numero = int(input('Digite um numero de 0 a 10: '))
    quantidade += 1

print('\033[32mVOCÊ ACERTOU APÓS {} tentativas\033[m'.format(quantidade))

# computador = randint(0, 10)
# acertou = False
# palpites = 0

# while not acertou:
#   jogador = int(input('Digite um numero de 0 a 10: '))
#   palpites += 1

#   if jogador == computador
#       acertou = True
#   else:
#       if jogador < computador:
#           print('Mais...')
#       elif jogador > computador:
#           print('Menos...')

# print ('Acertou depois de {} tentativas'.format(palpites))