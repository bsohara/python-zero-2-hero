def return_example():
    return print('retorno')

return_example()

def soma(a, b):
    return a + b

soma_return = soma(1, 2)
print(soma_return)

#retorna o nome ==> tarefa
def cliente(nome):
    print(f'Olá {nome}')

cliente('Maria')

#não tem retorno de nome
def cliente2(nome2):
    return nome2

x = cliente2('José')
print(x)