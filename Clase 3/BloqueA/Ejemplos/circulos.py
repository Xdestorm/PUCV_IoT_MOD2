from math import pi

#funciones
def perimetro(r):#
    return 2 * pi * r

def area(r):
    return pi * r ** 2
#progrma, la condicion if es para que no se ejecute si es importado
if __name__ == '__main__':
    n = float(input('Ingrese n: '))
    print('el perimetro es: ', perimetro(n))
