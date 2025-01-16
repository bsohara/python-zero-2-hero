from datetime import datetime

momento_atual = datetime.now()

ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = momento_atual.year
idade = ano_atual - ano_nascimento

print(f'A idade atual daquela pessoa: {int(idade)} anos.')