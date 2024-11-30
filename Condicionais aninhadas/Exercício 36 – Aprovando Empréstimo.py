v_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário comprador: R$'))
anos = int(input('Digite a quantidade de anos em que o comprador pagará: '))

# comprando casa R$200.000 e salario R$1000 e quer pagar em 50 anos (parcela mensal)
# valor da casa e dividir pela quantidade de parcelas de x anos
# pagar x reais por mes em 50 anos
# poder ou n pagar = nao pode exceder 30% do salario (PARCELA <= SALARIO * 0.3)

parcelas = v_casa / (anos * 12)

if parcelas <= salario * 0.3:
    print(' ')
    print('\033[34mEmprestimo aprovado!\033[m')
    print('As parcelas serão de \033[34mR${:.2f}\033[m divididas durante \033[34m{} meses'.format(parcelas, anos*12))
    print('30% do salário = \033[34mR${:.2f}\033[m e parcela = \033[34mR${:.2f}\033[m.'.format(salario * 0.3, parcelas, anos*12))

else: # mas podia ser elif tb
    print(' ')
    print('\033[31mEmprestimo negado.\033[m')
    print('30% do salário = \033[31mR${:.2f}\033[m e parcela = \033[31mR${:.2f}\033[m durante \033[31m{} meses\033[m.'.format(salario * 0.3, parcelas, anos*12))




