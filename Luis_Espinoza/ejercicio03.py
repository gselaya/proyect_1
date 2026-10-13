class SumaPromedio:
    def ejecutar(self):
        n = int(input("Cuantos numeros ingresara?: "))
        suma = 0
        for i in range(n):
            num = float(input("Ingrese un numero: "))
            suma += num
        promedio = suma / n if n > 0 else 0
        print(f"Suma: {suma}, Promedio: {promedio}")

if __name__ == "__main__":
    e = SumaPromedio()
    e.ejecutar()
