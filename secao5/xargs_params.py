def agencia(**carro):
    return carro


agencia1 = agencia(modelo='Gol', cor='Branca', motor=1.6, ano=2007, placa='ABC1D23')
print(agencia1)



def secao(**produto):
    # Entrada de dados
    nome = input('Nome: ')
    preco = float(input('Preço: R$ '))
    
    # Adiciona os dados ao dicionário recebido como argumento
    produto['nome'] = nome
    produto['preco'] = preco
    return produto

# Chamando a função e criando uma seção com dados
s1 = secao()
print(s1)