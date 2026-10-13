pares = 0
impares = 0
positivos = 0
negativos = 0

num = int(input("Ingrese un número (0 para terminar): "))

while num != 0:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if num > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

    num = int(input("Ingrese un número (0 para terminar): "))

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)