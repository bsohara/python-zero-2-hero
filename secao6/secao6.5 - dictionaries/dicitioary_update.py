aluno = {
    'nome': 'Bruno',
    'idade': 28,
    'RA': '2223970',
    'notas': [9.5, 9.0, 8.5, 9.0]
}

# atualizar um valor da forma comum
aluno['nome'] = 'Felipe'

print(aluno)

# atualizar um valor com update ==> dicionario.update({ 'chave': 'novo valor' })
aluno.update({ 'nome': 'Guilherme', 'idade': 22 })

print(aluno)

# inserir uma chave e um valor inexistente no dicionário
aluno.update({'endereco': 'Rua 123'})

print(aluno)

# inserir uma chave e um valor padrão
print(aluno.get('cidade', 'Não existe'))

# remover a chave de um dicionário
del aluno['notas']

print(aluno)
