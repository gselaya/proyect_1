n = int(input("¿Cuántas edades ingresará?: "))

ninos = 0
adolescentes = 0
adultos = 0
mayores = 0

for i in range(n):
    edad = int(input("Ingrese una edad: "))

    if edad >= 0 and edad <= 11:
        ninos = ninos + 1
    elif edad <= 17 and edad >= 12:
        adolescentes = adolescentes + 1
    elif edad <= 59 and edad >= 18:
        adultos = adultos + 1
    elif edad >= 60:
        mayores = mayores + 1
    else:
        print("Edad inválida")

print("Niños:", ninos)
print("Adolescentes:", adolescentes)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)