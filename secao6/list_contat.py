
'''

cidades_rmc = ['Campinas', 'Hortolândia', 'Paulínia', 'Indaiatuba', 'Valinhos']
cidades_abc = ['Santo André', 'São Bernardo do Campo', 'São Caetano do Sul', 'Diadema', 'Embu Guaçu']
cidades_lit_sant = ['Santos', 'Guarujá', 'Peruíbe', 'Praia Grande', 'São Vicente']

cidades_sp = cidades_lit_sant + cidades_rmc + cidades_abc

print(cidades_sp)

'''

numeros1 = [2, 3, 4, 5]
numeros2 = numeros1 * 2
print(numeros2)

letras = ['a', 'b', 'c', 'd']
tudo = numeros1 + letras
print(tudo)

numeros1.extend(letras)
print(numeros1)

itens = [['item-a', 'item-b'], ['item-c', 'item-d']]
print(itens)
print(itens[1])
print(itens[1][0])
print(itens[0][1])

pessoa = {
    'nome': 'Bruno',
    'idade': 28,
    'conhecimentos': [
        {
            'conhecimento1': 'Redes de computadores',
            'tecnologias': [
                {'tec1': 'DWDM'},
                {'tec2': 'DWDM'}
            ]
        },
        {
            'conhecimento2': 'Desenvolvimento de sistemas'
        }
    ]
}

print(pessoa['conhecimentos'][0]['tecnologias'][0]['tec1'])
