archivo = open('quijote.txt')
contador = 0
for linea in archivo:
    contador +=1
archivo.close()
print("las lineas del archivo son: ",contador)
