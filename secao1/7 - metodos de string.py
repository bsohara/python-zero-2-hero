#métodos de string
mensagem = "Eu adoro churrasco, lanche e pizza"


# em maiúsculo e minúsculo
maiusculo = mensagem.upper()
minusculo = mensagem.lower()

print("em maiúsculo:",maiusculo)
print("em minúsculo:",minusculo)

# substutui caracteres ou palavras na frase
mensagem_alterada = mensagem.replace("pizza", "comida japonesa")
print(mensagem_alterada)

mensagem_alterada2 = mensagem.replace("a", "i")
print(mensagem_alterada2)

# encontra o início da letra ou da palavra
encontrar_churrasco = mensagem.index("churrasco")

print("Onde começa?",encontrar_churrasco)

