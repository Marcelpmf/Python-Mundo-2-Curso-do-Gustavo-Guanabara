mulheres20 = 0
somadoridade = 0
maiorH = 0
nomeHV = ' '


for contador in range (1, 5):

    nome = str(input('\nDigite o nome da {}ª pessoa: '.format(contador)))

    idade = int(input('Digite a idade da {}ª pessoa: '.format(contador)))
    somadoridade += idade
    media = somadoridade/4

    sexo = str(input('Digite o sexo da {}ª pessoa (H ou M): '.format(contador)))

    if sexo == 'M' and idade < 20:
        mulheres20 += 1

    elif idade > maiorH and sexo == 'H':
        maiorH = idade
        nomeHV = nome

print('\nA média da idade do grupo foi \033[34m{}\033[m anos\n'
      'O homem mais velho é o \033[34m{}\033[m \n'
      'Existem \033[34m{}\033[m mulheres com menos de 20 anos'.format(media, nomeHV ,mulheres20))