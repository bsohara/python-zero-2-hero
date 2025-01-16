def addNum(a, b):
    return a + b

def subNum(a, b):
    return a - b

def mulNum(a, b):
    return a * b

def divNum(a, b):
    return a / b

def showOptions():
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão") 

def chosenOptions(c, a, b):
    operations = {
        1: lambda: addNum(a, b),
        2: lambda: subNum(a, b),
        3: lambda: mulNum(a, b),
        4: lambda: divNum(a, b)
    }

    return operations.get(c, lambda: None)()

def main():
    options = 1
    while options >= 0 and options < 5:
        num1 = int(input("Digite um número para num1: "))
        num2 = int(input("Digite um número para num2: "))

        showOptions()
        options = int(input("Digite uma opção de cálculo matemático: "))
        print(f"Resultado da operação de opção {options} =",chosenOptions(options, num1, num2))
        print("\n")



main()
