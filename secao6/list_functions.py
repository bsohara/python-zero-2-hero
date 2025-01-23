# funções dentro da lista
cidades_sp = ['Campinas', 'Guarulhos', 'Piracicaba', 'Mogi das Cruzes', 'Mogi Mirim', 'Sumaré']

print(cidades_sp)

#append
cidades_sp.append('Santo André') #resultado: ['Campinas', 'Guarulhos', 'Piracicaba', 'Mogi das Cruzes', 'Mogi Mirim', 'Sumaré', 'Santo André']

print(cidades_sp) 

#remove
cidades_sp.remove('Mogi das Cruzes')

print(cidades_sp) #resultado: ['Campinas', 'Guarulhos', 'Piracicaba', 'Mogi Mirim', 'Sumaré', 'Santo André']

#insert(index, valor)
cidades_sp.insert(-1, 'Ubatuba')

print(cidades_sp) #resultado: ['Campinas', 'Guarulhos', 'Piracicaba', 'Mogi Mirim', 'Sumaré', 'Ubatuba', 'Santo André']

#pop(valor)
cidades_sp.pop()

print(cidades_sp) #resultado: ['Campinas', 'Guarulhos', 'Piracicaba', 'Mogi Mirim', 'Sumaré', 'Ubatuba']

#sort()
cidades_sp.sort()

print(cidades_sp) #resultado: ['Campinas', 'Guarulhos', 'Mogi Mirim', 'Piracicaba', 'Sumaré', 'Ubatuba']