import datetime

data = datetime.date.today()

ano_atual = data.year


contagemMAIOR = 0
contagemMENOR = 0

for contador in range (1, 8):
    nascimento = int(input('Digite o ano do nascimento da {}ª pessoa: '.format(contador)))

    if ano_atual - nascimento >= 18:
        contagemMAIOR += 1

    else:
        contagemMENOR += 1

print('\nQuantidade de pessoas com MAIS de 18 anos: {}'
      '\nQuantidade de pessoas com MENOS de 18 anos: {}'
      .format(contagemMAIOR, contagemMENOR))





