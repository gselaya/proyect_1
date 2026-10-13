class MayorMenor:
    def ejecutar(self):
        mayor = None
        menor = None
        for i in range(10):
            num = int(input("Ingrese un numero: "))
            if i == 0:
                mayor = num
                menor = num
            else:
                if num > mayor:
                    mayor = num
                if num < menor:
                    menor = num
        print(f"Mayor: {mayor}, Menor: {menor}")

if __name__ == "__main__":
    e = MayorMenor()
    e.ejecutar()
