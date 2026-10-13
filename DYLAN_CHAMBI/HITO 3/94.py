mayores = 0
menores = 0

edad = int(input("Ingrese una edad (0 para terminar): "))

while edad != 0:
    if edad >= 18:
        mayores = mayores + 1
    else:
        if edad > 0:
            menores = menores + 1
        else:
            print("Edad inválida")

    edad = int(input("Ingrese una edad (0 para terminar): "))

print("Mayores de edad:", mayores)
print("Menores de edad:", menores)