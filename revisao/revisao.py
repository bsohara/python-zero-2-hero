departamentos = []
quantidade = int(input("Quantos departamentos têm na empresa? "))

for i in range(quantidade):

    departamento = {
        'nome': input("Qual o nome do departamento? "),
        'email': input("Qual o email de contato do departamento solicitado? ")
    }

    departamentos.append(departamento)

print('\nDepartametos cadastrados')
for d in departamentos:
    print(f'Nome do departamento: {d['nome']} || E-mail: {d['email']}')

