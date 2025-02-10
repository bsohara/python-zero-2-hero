aluno = {
    'nome': 'Bruno',
    'idade': 16,
    'nota_final': 'A',
    'aprovado': True
}

for a in aluno.keys():
    print(a)

for a in aluno.values():
    print(a)

for a in aluno.items():
    print(a)

for keys, values in aluno.items():
    print(keys, values)