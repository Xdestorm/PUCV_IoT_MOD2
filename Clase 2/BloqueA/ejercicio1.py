i = 0
n = int(input("Ingrese numero de alumnos: "))
suma = 0
while i < n:
    nota = int(input("ingrese nota de alumno " + str(i+1)+ ": "))
    suma+= nota
    i+=1
print("Promedio: ", suma/n)