class MenuBancario:
    def ejecutar(self):
        saldo = 0.0
        while True:
            print("\n1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
            opc = input("Opcion: ")
            if opc == "4":
                break
            elif opc == "1":
                print(f"Saldo actual: ${saldo}")
            elif opc == "2":
                monto = float(input("Monto a depositar: "))
                saldo += monto
            elif opc == "3":
                monto = float(input("Monto a retirar: "))
                if monto <= saldo:
                    saldo -= monto
                else:
                    print("Fondos insuficientes")

if __name__ == "__main__":
    e = MenuBancario()
    e.ejecutar()
