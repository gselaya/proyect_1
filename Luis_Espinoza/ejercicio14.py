class ClasificacionEdades:
    def ejecutar(self):
        n = int(input("Cuantas edades ingresara?: "))
        ninos = 0
        adolescentes = 0
        adultos = 0
        mayores = 0
        for i in range(n):
            edad = int(input("Ingrese edad: "))
            if edad <= 12:
                ninos += 1
            elif edad <= 17:
                adolescentes += 1
            elif edad <= 59:
                adultos += 1
            else:
                mayores += 1
        print(f"Ninos: {ninos}, Adolescentes: {adolescentes}, Adultos: {adultos}, Adultos mayores: {mayores}")

if __name__ == "__main__":
    e = ClasificacionEdades()
    e.ejecutar()
