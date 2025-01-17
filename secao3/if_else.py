velocidade = 100

if velocidade > 100:
    print("Velocidade maior do que a permitida. Abaixe para manter na velocidade permitida.")
elif velocidade <= 100 and velocidade > 40:
    print("Velocidade permitida. Tente manter nesta velocidade.")
else:
    print("Velocidade abaixo da permitida. Aumente a velocidade.")