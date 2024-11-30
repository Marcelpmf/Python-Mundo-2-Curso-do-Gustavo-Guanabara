#contador = 1
#while contador < 10:
    #print(contador)
    #contador += 1 # (pra ir aumentado ate 10)
#print('FIM')

# WHILE É BOM PRA INDEFINIDO E FOR PARA DEFINIDO

# ---------------------CONDIÇÃO DE PARADA 1-------------------------------- #

#numero = 1

#while numero != 0:
    #numero = int(input('Digite um valor: '))
#print('FIM')

# ---------------------CONDIÇÃO DE PARADA 2-------------------------------- #

#resposta = 'S'
#while resposta == 'S':
    #numero = int(input('Digite um número: '))
    #resposta = str(input('Quer continuar? [S/N] ')).upper()
#print('FIM')

# -------------------------------------------------------------------------- #

numero = 1 #(para nao cair no 0 (é gambiarra)
par = 0 # ou faz par = impar = 0
impar = 0

while numero != 0:
    numero = int(input('Digite um valor: '))

    if numero != 0: #(para nao ler o 0 como impar)
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print('Existem {} numeros pares e {} numeros impares'.format(par, impar))


