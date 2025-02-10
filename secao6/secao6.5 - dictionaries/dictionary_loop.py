aluno = {
    'nome': 'Bruno',
    'idade': 16,
    'nota_final': 'A',
    'aprovado': True
}

print()
for a in aluno.keys():
    print(a)

print()
for a in aluno.values():
    print(a)

print()
for a in aluno.items():
    print(a)

print()
for keys, values in aluno.items():
    print(keys,"=", values)