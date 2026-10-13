class TiendaProductos:
    def ejecutar(self):
        total = 0
        while True:
            print("\n1. Ingresar producto\n2. Finalizar")
            opc = input("Opcion: ")
            if opc == "2":
                break
            elif opc == "1":
                prod = input("Nombre producto: ")
                precio = float(input("Precio: "))
                total += precio
        print(f"Total a pagar: {total}")

if __name__ == "__main__":
    e = TiendaProductos()
    e.ejecutar()
