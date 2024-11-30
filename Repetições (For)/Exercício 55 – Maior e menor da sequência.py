maiorP = 0
menorP = 0

for contador in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(contador)))

    if peso == 1: # peso da primeira pessoa
        maiorP = peso # vai ser o primeiro
        menorP = peso # vai ser o primeiro tb

    else: # se nao for o peso da primeira pessoa
        if peso > maiorP:
            maiorP = peso
        if peso < menorP:
            menorP = peso

print('\nMaior peso {} e menor peso {}'.format(maiorP, menorP))
