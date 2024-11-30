valor = float(input('Digite o valor do produto: R$'))

forma = int(input(
                  '1 - A vista no dinheiro / Cheque\n' # 10% de desconto
                  '2 - A vista no cartão\n' # 5% de desconto
                  '3 - 2x no cartão\n' # normal
                  '4 - 3x ou mais no cartao\n' # 20% a mais
                  'DIGITE O NUMERO DA FORMA DE PAGAMENTO: '))

if forma == 1:
    print('Valor final do produto: R${:.2f}'.format(valor * 0.90))

elif forma == 2:
    print('Valor final do produto: R${:.2f}'.format(valor * 0.95))

elif forma == 3:
    parcela = valor / 2
    print('Valor final do produto: R${:.2f} e duas parcelas de R${:.2f}'.format(valor, parcela))

elif forma == 4:
    total = valor + (valor * 20 / 100)
    parcelaToT = int(input('Quantas parcelas? '))
    parcela = total / parcelaToT

    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcelaToT, parcela))
    print('Valor final do produto: R${:.2f}'.format(valor * 1.20))

else:
    print('Opção inválida! tente novamente.')

