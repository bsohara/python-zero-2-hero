fruit = "Fruta do conde"
#index   01234567890123

'''
pegar porções de uma palavra ou texto
'''

a = int(input("Qual index para 'a'? "))
b = int(input("Qual index para 'b'? "))

showCharIntervals = fruit[a:b]

print(showCharIntervals)

'''
slice para números flutuantes
--> não é mostrado, porque não é subscritible
--> então, o que deveria ser feito? 
    a. converter a variável float para string
    b. encontrar o valor determinado, que seria no caso, os centavos
'''
salary = 1999.75
#index = 0123456
cents = str(salary)

print(f"Valor dos centavos: {cents[5:7]}")