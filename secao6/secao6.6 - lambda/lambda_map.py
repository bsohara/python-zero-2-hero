lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def multi(x):
    return x * 2

listax2 = map(multi, lista1)
print(list(listax2))

# map com lambda

lista3 = map(lambda x: x*3, lista1)
print(list(lista3))

print(list(map(lambda a: a * 5, lista1)))

#quadrado de lista de números
print(list(map(lambda n: n ** 2, lista1)))