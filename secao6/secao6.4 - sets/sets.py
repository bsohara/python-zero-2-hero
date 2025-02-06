'''

set ( listas )
- similar a lists
- evita itens duplicados
- não utiliza index

'''

list1 = [10, 20, 30, 30, 40, 50, 60, 70]
list2 = [10, 20, 80, 90, 100]

num1 = set(list1) #perde a indexação
num2 = set(list2)

print("Union: ", num1 | num2) # union => retira dados duplicados e une duas listas

print("Difference: ", num1 - num2) # difference => insere os elementos em comum em duas ou mais listas

print ("Symetric difference: ", num1 ^ num2) # symetric difference => mostra os valores únicos

print ("And: ", num1 & num2) # and => mostra elementos duplicados em duas ou mais listas

print(len(num1)) #len => verifica a quantidade de elementos de uma lista