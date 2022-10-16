n_mayor = 0
k = 1
c = int(input("Escriba la cantidad de numeros que desea comparar " + str(k) + ": "))
while k <= c:
    n = float(input("Digitar numero: "))
    if n > n_mayor:
        n_mayor = n
        posicion = k
    else:
        n_mayor = n_mayor
    k += 1
print ("El mayor numero es: ",n_mayor, "la posicion es: ", posicion)