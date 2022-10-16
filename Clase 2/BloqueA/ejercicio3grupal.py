
n = int(input('ingrese numero: '))

if n > 0:
    resto= n%2
    if resto != 0:
        print('es primo')
    else:
        print('no es primo')
else:
    print('ingrese un numeor mayor que 0')


