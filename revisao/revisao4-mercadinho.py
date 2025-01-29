produtos = []
opcoes = ['1 - Adicionar produtos', '2 - Visualizar todos os produtos', '3 - Verificar total de produtos', '4 - Remover produto']

def visualiza_opcoes():
    for op in opcoes:
        print(op)

def metodos_opcoes(a):
    match a:
        case 1:
            produtos.append(produtos)

        case 2:
            for p in produtos:
                print(p)

        case 3:
            p = len(produtos)
            print(f"Quantidade de produtos: {p} produtos.")


visualiza_opcoes()
