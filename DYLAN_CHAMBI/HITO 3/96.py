total = 0
opcion = "S"

while opcion == "S":
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))

    total = total + precio

    print("Producto:", producto)
    print("Precio:", precio)

    opcion = input("¿Desea ingresar otro producto? (S/N): ").upper()

print("Total a pagar:", total)