class NotasEstudiantes:
    def ejecutar(self):
        suma = 0
        cant = 0
        mayor = None
        menor = None
        while True:
            nota = float(input("Ingrese nota (-1 para terminar): "))
            if nota == -1:
                break
            suma += nota
            cant += 1
            if mayor is None or nota > mayor:
                mayor = nota
            if menor is None or nota < menor:
                menor = nota
        if cant > 0:
            print(f"Promedio: {suma / cant}, Mayor: {mayor}, Menor: {menor}")

if __name__ == "__main__":
    e = NotasEstudiantes()
    e.ejecutar()
