numero = somador = 0

while True:
    numero = int(input('Digite um numero: '))

    if numero == 999:
        break

    somador += numero

#print('A soma vale {}'.format(somador))

print(f'A soma vale {somador}') # f strings interpolação melhor assim

# {somador:.2f} exemplo // {somador:^20} 20 caracteres centralizados // {somador:-<20} aninhar a esquerda
