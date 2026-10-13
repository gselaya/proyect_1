n = int(input("¿Cuántos números ingresará?: "))
suma = 0

for i in range(n):
    num = float(input("Ingrese un número: "))
    suma = suma + num

if n > 0:
    promedio = suma / n
    print("La suma es:", suma)
    print("El promedio es:", promedio)
else:
    print("Debe ingresar una cantidad mayor que cero")