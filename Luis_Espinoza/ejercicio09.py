class RegistroEdades:
    def ejecutar(self):
        mayores = 0
        menores = 0
        while True:
            edad = int(input("Ingrese edad (0 para salir): "))
            if edad == 0:
                break
            if edad >= 18:
                mayores += 1
            else:
                menores += 1
        print(f"Mayores de edad: {mayores}, Menores de edad: {menores}")

if __name__ == "__main__":
    e = RegistroEdades()
    e.ejecutar()
