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

# criar uma frase e imprimir
# O Bruno tem 28 anos de idade e mora na cidade de São Paulo

nome = "Bruno"
idade = int(20)
cidade = "São Paulo"
print(f"O {nome} tem {idade} e mora na cidade de {cidade}") # >> f' string

# Bruno quer se tornar programador python e analista de redes de computadores e telecomunicações
outro_nome = "Bruno"
profissao = {
    'prof1': 'programador',
    'prof2': 'analista de redes de computadores e telecomunicações'
}

profissao['prof1'] = 'esteticista'

print(f"{outro_nome} quer ser {profissao['prof1']} e {profissao['prof2']}.")