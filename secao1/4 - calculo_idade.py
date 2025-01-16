from datetime import datetime

momento_atual = datetime.now()

ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = momento_atual.year
idade = ano_atual - ano_nascimento

print(type(ano_nascimento), ' - ', type(ano_atual), ' - ', type(idade))


print(f'A sua idade atual: {int(idade)} anos.')