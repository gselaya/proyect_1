saldo = 1000
opcion = 0

while opcion != 4:
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Saldo actual:", saldo)

    elif opcion == 2:
        cantidad = float(input("Ingrese el depósito: "))

        if cantidad > 0:
            saldo = saldo + cantidad
            print("Depósito realizado")
        else:
            print("Cantidad inválida")

    elif opcion == 3:
        cantidad = float(input("Ingrese el retiro: "))

        if cantidad > 0 and cantidad <= saldo:
            saldo = saldo - cantidad
            print("Retiro realizado")
        else:
            print("Fondos insuficientes o cantidad inválida")

    elif opcion != 4:
        print("Opción inválida")

print("Gracias por utilizar el banco")