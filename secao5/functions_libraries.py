'''
Funções = maçã (cor, R$, peso); banana (cor, R$, peso)

Módulos = sessões frutas e verdutas; sessão de beleza;

Pacote = supermecado A (brasileiras); supermercado B (norueguesa)

Bibliotecas = hipermercado A
'''

# como funciona uma função???
def imprime_nome():
    print("Olá Bruno!")

imprime_nome()


# criando uma função de soma
# variáveis não pertencentes à função ==> global

def soma_dois_numeros():
    num1 = 10
    num2 = 22
    #variáveis pertencentes à função ==> escopo
    resultado = num1 + num2
    print(resultado)

def soma_dois_numeros1():
    num1 = 10
    num2 = 1
    #variáveis pertencentes à função ==> escopo
    resultado = num1 + num2
    print(resultado)

soma_dois_numeros()
soma_dois_numeros1()
