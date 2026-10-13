opcion = 0

while opcion != 5:
    print("1. Factorial")
    print("2. Tabla de multiplicar")
    print("3. Saber si es par o impar")
    print("4. Calcular cuadrado")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        num = int(input("Ingrese un número: "))

        if num >= 0:
            factorial = 1

            for i in range(1, num + 1):
                factorial = factorial * i

            print("Factorial:", factorial)
        else:
            print("No se admite un número negativo")

    elif opcion == 2:
        num = int(input("Ingrese un número: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif opcion == 3:
        num = int(input("Ingrese un número: "))

        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")

    elif opcion == 4:
        num = float(input("Ingrese un número: "))
        print("Cuadrado:", num * num)

    elif opcion != 5:
        print("Opción inválida")

print("Programa finalizado")