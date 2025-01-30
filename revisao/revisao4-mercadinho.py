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

confirmar = ''

while True:
        print("=== Mercadinho do Pai ===")
        visualiza_opcoes()
        opcao = int(input("Digite a opção que deseja: "))
        match opcao:
            case 1:
                produto = input("Digite o produto para adicionar no mercado: ")
                adiciona_produto(produto)
            case 2:
                mostra_produtos()
            case 3:
                produto = input("Digite o produto para remover no mercado: ")
                remove_produto(produto)
            case _:
                print("Opção não existe.")


        confirmar = input("Continuar? [s/n]")






