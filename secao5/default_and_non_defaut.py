'''
Funções (functions)
    - a. DRY ==> don't repeat yourself
    - b. Parâmetros ==> argumentos
    - c. Default ==> valor definido no parâmetro
    - d. Non-default ==> valor não definido no parâmetro

    ==> default e non-default devem estar em uma ordem

    No exemplo abaixo, a variável 'nome' terá um nome de um produto. Então deverá ser passado.
    Já na variável 'quantidade', como já foi definida no parâmetro, não será necessário passar na chamada da função
'''

def produto(nome, preco=10.99):
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco}")

produto("chocolate")
produto("chocolate", 9.99) #sobescrita