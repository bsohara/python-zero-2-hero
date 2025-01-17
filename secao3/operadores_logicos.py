'''
and => dois critérios devem ser aprovados. Caso um dos critérios sejam verdadeiros, dará como 'False'.
or => um dos critérios podem ser aprovados

renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado!')
else:
    print('Financiamento negado!')

'''

# quem pode participar do concurso público?
formado = True
diploma_emitido = True
exepriencia = False

if formado and diploma_emitido and exepriencia:
    print("Você pode participar!")
elif (formado and diploma_emitido) or exepriencia:
    print("Você pode participar do processo. Mas será verificado no seu currículo.")
else:
    print("Você não pode participar.")