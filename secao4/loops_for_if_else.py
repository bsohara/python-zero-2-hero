'''
for i in range(20):
    if i % 2 == 0:
        print(f'{i} é um número par.')

'''

quitado = False


def dadosQuitacao():
    titulo = 'Dados de Quitação'

    print(f'{titulo.center(50)}')
    print('=================================================')
    print('|Parcelas pagas: 72                             |')
    print('|Última parcela paga: 17/01/2025                |')
    print('=================================================')

for n in range(3):
    if quitado:
        print("Contas quitadas. Que tal investir seu dinheiro para render?")
        dadosQuitacao()
        break
    else:
        print("Ainda não foi quitada. Veja qual parcela restante para pagar.")
        break