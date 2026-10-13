class EstadisticasNotas:
    def ejecutar(self):
        aprobados = 0
        reprobados = 0
        suma = 0
        for i in range(10):
            nota = float(input("Ingrese nota (0-100): "))
            suma += nota
            if nota >= 51:
                aprobados += 1
            else:
                reprobados += 1
        print(f"Aprobados: {aprobados}, Reprobados: {reprobados}, Promedio: {suma / 10}")

if __name__ == "__main__":
    e = EstadisticasNotas()
    e.ejecutar()
