archivo = open('quijote.txt')
lineab = ""
for linea in archivo:
    linea = linea.replace(" ",",").strip()
    lineab += linea
print("las palabras que tiene el archivo son : ",len(lineab.split(",")))

archivo.close()