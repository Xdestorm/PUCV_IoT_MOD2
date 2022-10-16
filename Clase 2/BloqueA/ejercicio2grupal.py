##Completar
i = 0
contador = 0
n = int(input('ingrese numero: '))
while i < n:

    if n <= 0:
        print('Error, debe ingresar un numero mayor a 0')
    elif num % 2 != 0:
        contador +=1
    i += 1
print('los impares son: ', contador)
