def soma(*numeros):
    r = 0
    for numero in numeros:
        r += numero
    return r


x = soma(1,2,3,4,5,6,7)
print(x)

def subtracao(*numeros2):
    r = 100
    for numero2 in numeros2:
        r -= numero2
    return r

y = subtracao(10, 20, 30)
print(y)