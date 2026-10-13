n = int(input("¿Cuántos números ingresará?: "))

positivos = 0
negativos = 0
ceros = 0

for i in range(n):
    num = float(input("Ingrese un número: "))

    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)