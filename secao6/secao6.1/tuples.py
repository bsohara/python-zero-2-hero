'''
- Tuples => gasto de armazenamento menor em comparação com listas
    - armazenar mais de uma informação em variáveis
    - manter a sequência dos dados em uma variável
    - não devem ser alteradas, diferente das listas

'''

cores_lista = ['amarelo', 'verde', 'azul', 'vermelho'] # utilização de colchetess
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho') # utilização de parenteses

'''
print(cores_lista)
print(cores_tuple)

print(type(cores_lista))
print(type(cores_tuple))

print(cores_lista * 2)

'''

cores_lista.append('laranja')
print(cores_lista)

cores_tuple.append('laranja')
print(cores_tuple)

# resultado: 'tuple' object has no attribute 'append' => não é possível alterar algo relacionado com tuple