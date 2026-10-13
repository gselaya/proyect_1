nota = float(input("Ingrese una nota (-1 para terminar): "))

suma = 0
cantidad = 0

while nota != -1:
    suma = suma + nota
    cantidad = cantidad + 1

    if cantidad == 1:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

    nota = float(input("Ingrese una nota (-1 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("Promedio:", promedio)
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
else:
    print("No se ingresaron notas")