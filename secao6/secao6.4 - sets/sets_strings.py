'''

sets com strings

- operadores de sets com strings


'''


set1 = {'a', 'b', 'c'}
set2 = {'a', 'b', 'd', 'e'}
set3 = {'a', 'c', 'f', 'g'}

set4 = set1.union(set2)                  # union ==> união de sets sem que apareça diferentes
set5 = set1.difference(set3)             # difference ==> diferença de valores
set6 = set1.intersection(set2)           # intersection ==> o mesmo valor aparece nas duas listas
set7 = set1.symmetric_difference(set3)   # symetric_difference ==> retira os valores duplicados

print(set4)

print(set5)

print(set6)

print(set7)