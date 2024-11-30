import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = datetime.date.today()

idade = ano_atual.year - ano_nascimento


print('você tem {} anos'.format(idade))

if idade <= 9:
    print('MIRIM')

elif idade >= 9 and idade <= 14:
    print('INFANTIL')

elif idade >= 14 and idade <= 19:
    print('JUNIOR')

elif idade >= 19 and idade <= 20:
    print('SÊNIOR')

else:
    print('MASTER')
