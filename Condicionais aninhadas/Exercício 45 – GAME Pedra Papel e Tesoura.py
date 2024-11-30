import random

print('======================\nPEDRA PAPEL E TESOURA\n======================')

opcUs = int(input('Escolha sua opção (Pedra, Papel ou tesoura):\n'
                '1 - Pedra\n'
                '2 - Papel\n'
                '3 - tesoura\n'
                  'Digite a sua opção: '))

opcPC = int(random.randint(1,3))

if  opcUs == 1:
    print('\033[34mVocê escolheu Pedra\033[m')
elif opcUs == 2:
    print('\033[34mVocê escolheu Papel\033[m')
elif opcUs == 3:
    print('\033[34mVocê escolheu Tesoura\033[m')
else:
    print('Opção inválida.')
# ---------------------------------------------- #

if  opcPC == 1:
    print('\033[33mO PC escolheu Pedra\033[m')
elif opcPC == 2:
    print('\033[33mO PC escolheu Papel\033[m')
elif opcPC == 3:
    print('\033[33mO PC escolheu Tesoura\033[m')

# ------------------- JOGO ---------------------- #

if opcUs == 1 and opcPC == 2: # pedra contra papel PC ganha
    print('O PC ganhou')
elif opcUs == 1 and opcPC == 3: # pedra contra tesoura voce ganha
    print('Você ganhou')

elif opcUs == 2 and opcPC == 1: # papel contra pedra voce ganha
    print('Você ganhou')

elif opcUs == 2 and opcPC == 3: # papel contra tesoura PC ganha
    print('O PC ganhou')

elif opcUs == 3 and opcPC == 2: # tesoura contra papel voce ganha
    print('Você ganhou')

elif opcUs == 3 and opcPC == 1: # tesoura contra pedra o PC ganha
    print('O PC ganhou')

elif opcUs == opcPC:
    print('EMPATE!')

