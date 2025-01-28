maioridade = []
menoridade = []

while True:
    idade = int(input("Qual a idade? "))

    if 18 <= idade <= 100:
        print("Maior de idade")
        maioridade.append(idade)
    elif 0 < idade < 18:
        print("Menor de idade")
        menoridade.append(idade)
    else:
        break

print(f'Lista de idades (maior de idade): {maioridade}')
print(f'Lista de idades (menor de idade): {menoridade}')

idades = zip(maioridade, menoridade)
print(list(idades))