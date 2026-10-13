opcion = 0

while opcion != 5:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion >= 1 and opcion <= 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado:", a + b)
        elif opcion == 2:
            print("Resultado:", a - b)
        elif opcion == 3:
            print("Resultado:", a * b)
        elif opcion == 4:
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("No se puede dividir entre cero")
    elif opcion != 5:
        print("Opción inválida")

print("Hasta luego")