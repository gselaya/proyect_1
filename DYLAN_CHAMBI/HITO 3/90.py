respuesta = "S"

while respuesta == "S":
    num = int(input("Ingrese un número: "))

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

    respuesta = input("¿Desea repetir? (S/N): ").upper()

print("Programa finalizado")