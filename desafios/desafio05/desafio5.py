def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero não é permitida."

def exponenciacao(a, b):
    return a ** b

def imprime_calculos(a, b):
    print(f'Resultado da adição = {adicao(a, b)}')
    print(f'Resultado da subtração = {subtracao(a, b)}')
    print(f'Resultado da multiplicação = {multiplicacao(a, b)}')
    print(f'Resultado da divisão = {divisao(a, b)}')
    print(f'Resultado da exponenciação = {exponenciacao(a, b)}')

def main():
    try:
        a = int(input("Qual valor para a? "))
        b = int(input("Qual valor para b? "))
        imprime_calculos(a, b)
    except ValueError:
        print("Erro: por favor, insira apenas números inteiros.")

if __name__ == "__main__":
    main()