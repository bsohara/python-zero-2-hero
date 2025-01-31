'''
produtos = ['abacaxi', 'uva', 'banana', 'goiaba']
valores = [1.99, 13.99, 10.99, 8.99]



v = ['comprar'] #==> c o m p r a r
var = list('comprar') #built-in ==> inserido no proprio python, sem necessidade de implantação
print(var)

duas_listas = zip(produtos, valores)
print(list(duas_listas)) #==> uma tupla em uma lista

'''
numero_carros = int(input("Quantos carros estarão na lista? "))

marcas = []
modelos = []
anos = []
motores = []

carros = zip(marcas, modelos, anos, motores)

for i in range(numero_carros):
    marca = input("Qual a marca do carro? ")
    modelo = input("Qual modelo do carro? ")
    ano = int(input("Qual ano deste carro? "))
    motor = float(input("Qual o motor deste carro? "))

    marcas.append(marca)
    modelos.append(modelo)
    anos.append(ano)
    motores.append(motor) 

print(list(carros))


