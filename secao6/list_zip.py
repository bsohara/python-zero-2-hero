produtos = ['abacaxi', 'uva', 'banana', 'goiaba']
valores = [1.99, 13.99, 10.99, 8.99]



v = ['comprar'] #==> c o m p r a r
var = list('comprar') #built-in ==> inserido no proprio python, sem necessidade de implantação
print(var)

duas_listas = zip(produtos, valores)
print(list(duas_listas)) #==> uma tupla em uma lista