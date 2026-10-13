class TablaMultiplicarRepetir:
    def ejecutar(self):
        while True:
            num = int(input("Ingrese un numero para la tabla: "))
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
            opc = input("Desea probar otro numero? (s/n): ")
            if opc.lower() != 's':
                break

if __name__ == "__main__":
    e = TablaMultiplicarRepetir()
    e.ejecutar()
