nome = str(input('Digite seu nome: '))

if nome == 'eu':
    print('oi, {}. Nome massa'.format(nome))

elif nome == 'curso' or nome == 'animal': # pode usar elif quantas vezes vc quiser
    print('Seu nome é popular, {}'.format(nome))

elif nome in 'frieda dandara cachorro bambi': # muitos de uma so vez
    print('Que nome bonito, {}'.format(nome))

else:
    print('Simples')
    
print('Tenha um bom dia {}'.format(nome))