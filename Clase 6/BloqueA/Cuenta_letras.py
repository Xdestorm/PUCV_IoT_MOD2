archivo = open('quijote.txt')
lineab = ""
for linea in archivo:
    linea = linea.replace(" ","").strip()
    lineab += linea
print("la cantidad de letras del texto son : ",len(lineab))
archivo.close()