contadorH = contadorMM20 = maisde18 =  0


while True:

    idade = int(input('\nIdade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        maisde18 += 1
    if sexo == 'M':
        contadorH += 1
    if sexo == 'F' and idade < 20:
        contadorMM20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break


print('='*10,'Fim do programa','='*10)

print(f'Total de pessoas com mais de 18 anos: {maisde18}'
      f'\nAo todo temos {contadorH} homens cadastrados'
      f'\nTemos {contadorMM20} mulheres com menos de 20 anos')

