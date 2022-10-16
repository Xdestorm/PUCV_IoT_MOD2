#Ejercicio 6
valor1 = float(input("ingrese lado a: "))
valor2 = float(input("ingrese lado b:"))
valor3 = float(input("ingrese lado c: "))

s = (valor1 + valor2 + valor3) / 2
d1 = s - valor1
d2 = s - valor2
d3 = s - valor3

prod = s * d1 * d2 * d3
area = prod ** .5
