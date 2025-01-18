"""
    Mercadinho
    ==========

1. Introdução
- criar um sisteminha de listagem de produtos e categorias
- o intuito deste projeto é revisar conceitos de Python


"""
produtos = []

for i in range(3):


    produto = {
        'nome': input("Digite o nome do produto: "),
        'preco': float(input("Digite o preço deste produto: R$ ")),
        'quantidade': int(input("Digite a quantidade deste produto: "))
    }

    produtos.append(produto)


for p in produtos:
    print(f'Nome: {p['nome']} == Preço: R${p['preco']:.2f} == Quantidade: {p['quantidade']}')