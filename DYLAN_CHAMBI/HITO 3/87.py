for i in range(10):
    num = int(input("Ingrese un número: "))

    if i == 0:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num

        if num < menor:
            menor = num

print("El mayor es:", mayor)
print("El menor es:", menor)