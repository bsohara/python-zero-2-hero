valoresFinais = []
quantidade = int(input("Digite quantos: "))

for i in range(quantidade):
    valor = int(input("Digite o valor a ser acrescido: "))

    while valor > 20:
        valor = valor + (valor * 0.1)
        valoresFinais.append(valor)
        break

for valorFinal in valoresFinais:
    print(f'Valor final do produto: R${valorFinal}')

    