primeiroT = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiroT # começa com o primeiro termo
contador = 1 # 10 primeiros termos contar quantos termos foram
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1

    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer: '))

print('FIM')

