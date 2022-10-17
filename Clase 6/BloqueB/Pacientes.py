pacientes = open("Pacientes.csv")
jovenes = open("jovenes.csv","w")
mayores = open("mayores.csv","w")

for v1 in pacientes:
    linea = list(v1.strip().split(";"))
    edad = int(linea[2])
    if edad < 30:
        jovenes.write(v1)
    if edad >60:
        mayores.write(v1)
pacientes.close()
jovenes.close()
mayores.close()
