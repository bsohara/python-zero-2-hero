'''
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
cidade = input("Onde você mora? ")

texto = f"{nome} tem {idade} e mora em {cidade}."

print(texto)

'''

nome = input("Qual seu nome? ")
profissao = input("Do que você trabalha? ")
objetivos_profissionais = input("Qual seu objetivo profissional? ")
conhecimento = input("Qual(is) é(são) seu(s) conhecimento(s)? ")
experiencia = input("Quais são suas experiências profissionais? ")

historia = f'{nome} é {profissao} e quer se tornar {objetivos_profissionais}. Possui conhecimento(s) em {conhecimento} e experiência(s) de {experiencia}.'


print(historia)