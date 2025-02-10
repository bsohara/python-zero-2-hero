valores = [10, 20, 30, 40, 50, 60, 70]


def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))             # resultado >> [30, 40, 50, 60, 70]
print(list(filter(lambda x: x < 50, valores)))      # resultado >> [10, 20, 30, 40]

