archivo = open("notas.txt")
archivo2 = open("reporte_notas.csv","w")
aprobado = ""
for v1 in archivo:
    linea = v1.strip().split(":")
    nombre = linea[0]
    notas  = list(map(float,linea[1:]))
    #print(notas)
    promedio = sum(notas) / len(notas)
    print(promedio)
    if promedio>=4.0:
        aprobado = "APROBADO"
    else:
        aprobado = "REPROBADO"
    print(nombre,aprobado)
    linea2 = '{};{}'.format(nombre,aprobado)+'\n'
    archivo2.write(linea2)

archivo.close()
archivo2.close()
