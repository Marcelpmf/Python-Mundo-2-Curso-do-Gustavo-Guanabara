from math import pow

peso = float(input('Digite sua massa corporal em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))

IMC =  peso / pow(altura, 2)

if IMC < 18.5:
    print('O seu IMC é \033[32m{:.2f}\033[m e você está \033[32mABAIXO DO PESO\033[m'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('O seu IMC é \033[34m{:.2f}\033[m e você está com o \033[34mPESO IDEAL\033[m'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('O seu IMC é \033[33m{:.2f}\033[m e você está \033[33mACIMA DO PESO\033[m'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('O seu IMC é \033[31m{:.2f}\033[m e você está com \033[31mSOBREPESO\033[m'.format(IMC))
else:
    print('O seu IMC é \033[31m{:.2f}\033[m e você está com \033[31mOBESIDADE MORBIDA\033[m'.format(IMC))

