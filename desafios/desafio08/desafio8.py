#desafio08
frutas = ['Maçã', 'banana', 'manga', 'uva']
print(frutas)

frutas[1] = 'morango' #adicionar no índice específico
print(frutas)

frutas.append('abacaxi') #adicionar no final da lista
print(frutas)

frutas[0:2] = ['goiaba', 'amora', 'abacate']
print(frutas)

frutas.insert(1, 'tomate')
print(frutas)

# desafio09
frutas2 = ['maçã', 'morango', 'manga', 'uva', 'abacate']

frutas2.remove('manga')
print(frutas2)

del frutas[-1]
print(frutas2)