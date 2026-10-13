aprobadas = 0
reprobadas = 0
suma = 0

for i in range(10):
    nota = float(input("Ingrese una nota: "))

    suma = suma + nota

    if nota >= 51:
        aprobadas = aprobadas + 1
    else:
        reprobadas = reprobadas + 1

promedio = suma / 10

print("Aprobadas:", aprobadas)
print("Reprobadas:", reprobadas)
print("Promedio general:", promedio)