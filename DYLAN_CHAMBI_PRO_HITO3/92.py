opcion = 0

while opcion != 4:
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado: "))
        print("Área:", lado * lado)

    elif opcion == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        print("Área:", base * altura)

    elif opcion == 3:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        print("Área:", base * altura / 2)

    elif opcion != 4:
        print("Opción inválida")

print("Programa finalizado")