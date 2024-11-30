# R$50 / R$20 / R$10 / R$1
# ir somando

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Que valor você quer sacar? R$'))

total = valor # montante (valor q precisa ser sacado)
cedula = 50 # cedula atual (começa com a de maior valor mas pode botar de 100 reais tb)
totalcedula = 0 # total de cedulas de uma determinada cedula

while True:

    if total >= cedula: # se puder tirar ou se total for maior ou igual a quantidade de cedulas
        total -= cedula # tirar cedula do valor
        totalcedula += 1 # cada vez que tira o total de cedula vira + 1

    else: # se n der pra tirar, verifica
        if totalcedula > 0: # para nao escrever oq tiver 0 cedulas
            print(f'Total de {totalcedula} cedulas de R${cedula}')
        if cedula == 50: # se nao conseguir tirar 50
            cedula = 20 # vira celula de 20 e vai diminuindo...
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0 # cada vez que muda as notas, o total volta a 0
        if totalcedula == 0: # para quando o total for igual a 0
            break
print('='*30)
print('Volte sempre!')

# pega montante e vai tirando cedulas ate nao dar mais
# vai somando



