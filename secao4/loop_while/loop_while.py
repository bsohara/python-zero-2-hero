'''
for...loop ==> quando sabe o que quer. ex: gire por 5 vezes
==========
- aplicado em um alcance
- como se fosse uma engrenagem ou roda


while...loop ==> não sabe quantas vezes você quer que gire, a não ser por uma condição
============
- aplicado uma condição
- enquanto a máquina esteja ligada, gire algumas vezes

'''

valor = 100.00
dia = 1
while valor > 0:
    dia += 1
    valor -= 10
    print(f"No dia {dia}, o produto será vendido por R$ {valor}")