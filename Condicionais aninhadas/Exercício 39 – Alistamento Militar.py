import datetime

ano = int(input('Digite o ano do seu nascimento: '))

ano_atual = datetime.date.today()

idade = ano_atual.year - ano

# 18 - idade = quantidade de anos
# idade - 18 = atraso

if idade < 18:
    print('Você tem {} anos de idade e ainda vai se alistar daqui a {} anos'.format(idade ,18 - idade))
elif idade == 18:
    print('Você tem que se alistar!')
else:
    print('Fazem {} anos que você deveria ter se alistado'.format(idade - 18))


