class Calculadora:
    def ejecutar(self):
        while True:
            print("\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir")
            opc = input("Seleccione opcion: ")
            if opc == "5":
                break
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            if opc == "1":
                print("Resultado:", a + b)
            elif opc == "2":
                print("Resultado:", a - b)
            elif opc == "3":
                print("Resultado:", a * b)
            elif opc == "4":
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Error: division por cero")

if __name__ == "__main__":
    e = Calculadora()
    e.ejecutar()
