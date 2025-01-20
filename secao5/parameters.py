nomes = ['Marcos', 'Ronaldo', 'Linda']
quantidades = [4, 5, 6]

def boas_vindas(nome, quantidade):
    print(f'Olá, {nome}')
    print(f'Temos {quantidade} laptops.')

for i in range(3):
    boas_vindas(nomes[i], quantidades[i])
