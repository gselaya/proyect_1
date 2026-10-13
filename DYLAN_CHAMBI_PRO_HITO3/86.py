pares = 0
impares = 0

for i in range(10):
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)