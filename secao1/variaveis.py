'''
Tipos de dados

textos                      numeros
- string                    - integer >> inteiro (1, 2, 3, 4)
- str(texto)                - float >> decimais ou frações (3.4, 4.5, 5.66, 6.777, 3.14159)

tipo booleano
- bool: verdadeiro ou falso / true ou false / 0 ou 1 (em binários)

variáveis ==> um container pra armazenamento de dados

|    2     | ==> integer conteiner da variável x

|  "óleo"  | ==> string conteiner da variável y

x = 2
y = "olá"
'''

x = 2
y = "olá"
z = True

print(x, y, z)
print( x / 16)


# modificação e manipulação de dados
a = str(3)
b = int(4)
c = float(5) # >. converte de inteiro para decimal

print(a + a) # aqui se deu uma concatenação de variáveis do tipo string. resultado: 33
print(b + b) # soma dos inteiros. resultado: 8
print(c + c) # soma de decimais. resultado: 10.0