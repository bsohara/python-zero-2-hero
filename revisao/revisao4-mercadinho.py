produtos = []
opcoes = ['1 - Adicionar produtos', '2 - Visualizar todos os produtos', '3 - Remover produto']

def visualiza_opcoes():
    for op in opcoes:
        print(op)

def adiciona_produto(produto):
    if produto.lower() in produtos:
        print("Já existe este produto")
    else:
        produtos.append(produto)
        print("Produto adicionado no mercado.")

def mostra_produtos():
    print(f"Produtos cadastrados: {produtos}")

def remove_produto(produto):
    produtos.remove(produto)
    print("Produto removido no mercado.")

print("=== Mercadinho do Pai ===")
visualiza_opcoes()
#opcoes = int(input("Digite a opção que deseja: "))




