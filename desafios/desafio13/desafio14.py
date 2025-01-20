print('Loop com BREAK;')

for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)

print('Loop com CONTINUE;')
for numero in range(1, 11):
    if numero == 5:
        print('sai!')
        continue
    print(numero)

