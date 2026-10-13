respuesta = input("¿Desea continuar? (S/N): ").upper()

while respuesta != "S" and respuesta != "N":
    print("Opción inválida")
    respuesta = input("Ingrese S o N: ").upper()

print("Respuesta válida:", respuesta)
