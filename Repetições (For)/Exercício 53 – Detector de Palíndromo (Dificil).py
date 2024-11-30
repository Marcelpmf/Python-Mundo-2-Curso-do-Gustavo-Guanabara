frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print('Você digitou a frase {}'.format(junto))

for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('É UM PALINDROMO')
else:
    print('NÃO É PALINDROMO')

#frase = input("Qual a frase? ").upper().replace(" ", "")
#if frase == frase[::-1]:
    #print("A frase é um palíndromo")
#else:
    #print("A frase não é um palíndromo")