class ContarParesImpares:
    def ejecutar(self):
        pares = 0
        impares = 0
        for i in range(10):
            num = int(input("Ingrese un numero: "))
            if num % 2 == 0:
                pares += 1
            else:
                impares += 1
        print(f"Pares: {pares}, Impares: {impares}")

if __name__ == "__main__":
    e = ContarParesImpares()
    e.ejecutar()
