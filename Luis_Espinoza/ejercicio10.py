class AnalisisNumeros:
    def ejecutar(self):
        pares = 0
        impares = 0
        pos = 0
        neg = 0
        while True:
            num = int(input("Ingrese numero (0 para salir): "))
            if num == 0:
                break
            if num % 2 == 0:
                pares += 1
            else:
                impares += 1
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        print(f"Pares: {pares}, Impares: {impares}, Positivos: {pos}, Negativos: {neg}")

if __name__ == "__main__":
    e = AnalisisNumeros()
    e.ejecutar()
