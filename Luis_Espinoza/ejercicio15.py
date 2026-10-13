class MenuMatematico:
    def ejecutar(self):
        while True:
            print("\n1. Factorial\n2. Tabla de multiplicar\n3. Paridad\n4. Cuadrado\n5. Salir")
            opc = input("Opcion: ")
            if opc == "5":
                break
            num = int(input("Ingrese un numero: "))
            if opc == "1":
                fact = 1
                for i in range(1, num + 1):
                    fact *= i
                print(f"Factorial: {fact}")
            elif opc == "2":
                for i in range(1, 11):
                    print(f"{num} x {i} = {num * i}")
            elif opc == "3":
                if num % 2 == 0:
                    print("Es Par")
                else:
                    print("Es Impar")
            elif opc == "4":
                print(f"Cuadrado: {num ** 2}")

if __name__ == "__main__":
    e = MenuMatematico()
    e.ejecutar()
