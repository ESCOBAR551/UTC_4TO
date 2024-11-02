import math

print("¿Qué deseas calcular de un triángulo equilátero?")
print("1. Perímetro")
print("2.1 Área")
opcion = int(input("Ingresa 1 o 2: "))

if opcion == 1:
    lado = float(input("Ingresa la longitud de un lado: "))
    perimetro = 3 * lado
    print("El perímetro es:", perimetro)

elif opcion == 2:
    lado = float(input("Ingresa la longitud de un lado: "))
    area = (math.sqrt(3) / 4) * lado ** 2
    print("El área es:", area)

else:
    print("Opción no válida.")
