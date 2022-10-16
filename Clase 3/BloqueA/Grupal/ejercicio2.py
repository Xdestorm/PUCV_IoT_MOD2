def discriminante (a,b,c):
    resultado = b ** 2 - 4 * a * c
    return resultado

a = float(input('Ingrese le valor a: '))
b = float(input('Ingrese le valor b: '))
c = float(input('Ingrese le valor c: '))

resultado = discriminante(a,b,c)

if resultado < 0:
    print('la ecuacion no tiene soluciòn real')
elif resultado == 0:
    sol = -b / (2 * a)
    print('La soluciòn es unica y es ', sol)
else:
    sol1 = (-b - (resultado ** 0.5)) / (2 * a)
    sol2 = (-b + (resultado ** 0.5)) / (2 * a)
    print('La soluciòn 1 es: ', sol1)
    print('La soluciòn 2 es: ', sol2)