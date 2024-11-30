# numero = numero + (posicao - 1) x razao

primeiroT = int(input('Digite o primeiro termo da PA: '))
razao = int(input('digite a razão da PA: '))

decimo_T = primeiroT + (10 - 1) * razao

for contador in range (primeiroT, decimo_T + razao, razao):
    print('{} '.format(contador), end=' -> ')

print('FIM')

