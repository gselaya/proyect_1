class FigurasGeometricas:
    def ejecutar(self):
        while True:
            print("\n1. Cuadrado\n2. Triangulo\n3. Circulo\n4. Salir")
            opc = input("Seleccione figura: ")
            if opc == "4":
                break
            if opc == "1":
                l = float(input("Lado: "))
                print("Area:", l * l)
            elif opc == "2":
                b = float(input("Base: "))
                h = float(input("Altura: "))
                print("Area:", (b * h) / 2)
            elif opc == "3":
                r = float(input("Radio: "))
                print("Area:", 3.1416 * r * r)

if __name__ == "__main__":
    e = FigurasGeometricas()
    e.ejecutar()
