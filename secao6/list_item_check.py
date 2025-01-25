cores = ['azul', 'vermelho', 'verde', 'roxo', 'amarelo']
cor = input('Digite uma cor: ')

if cor.lower() in cores:
    print('Cor está inserida')
else:
    print('Cor não está disponível')
    cores.append(cor)
    print(f'Cor {cor} inserida na lista')

print(cores)