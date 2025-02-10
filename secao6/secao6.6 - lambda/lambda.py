'''

funções lambda
- muito utilizada dentro de outras funções


'''

def soma_numeros(x, y):
    return x + y

resultado_soma = soma_numeros(1,2)
print(resultado_soma)

soma_lambda = lambda a, b: a + b
print(soma_lambda(2,1))
