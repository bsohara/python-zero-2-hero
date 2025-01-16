grades = []
diferentials = []
x = int(input("Quantas notas serão inseridas? "))

for i in range(x):
    grade = float(input(f"Qual será a nota da posição {i}? => "))
    diferential = int(input(f"Qual o peso desta nota? => "))

    grades.append(grade)
    diferentials.append(diferential)

print(f"Notas: {grades}")
print(f"Pesos destas notas: {diferentials}")

for i in range(x):
    results = []
    
    for j in range(x):
        resultado = grades[j] * diferentials[j]
        results.append(resultado)

numerator = 0
denominator = 0

print(f"Resultados finais: {results}")

for i in range(len(results)):
    result = float(results[i])
    diferential = int(diferentials[i])
    numerator += result
    denominator += diferential

final_average = numerator / denominator

print(f"A média deste cidadão: {final_average}")