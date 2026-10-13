class PositivosNegativosCero:
    def ejecutar(self):
        n = int(input("Cuantos numeros ingresara?: "))
        pos = 0
        neg = 0
        cero = 0
        for i in range(n):
            num = float(input("Ingrese un numero: "))
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
            else:
                cero += 1
        print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {cero}")

if __name__ == "__main__":
    e = PositivosNegativosCero()
    e.ejecutar()
