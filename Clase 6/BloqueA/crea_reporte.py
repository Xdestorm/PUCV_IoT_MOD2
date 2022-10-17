temp1 = {
	'Vina del mar': (9, 26),
	'Valparaiso': (10, 24),
	'Quilpue': (7, 30),
	'Quintero': (4, 22)
	}

def crea_reporte(temp):
	archivo = open("reporte.txt", "w")
	lineab = ""

	for v1 in temp.keys():
		a,b = temp[v1]
		lineab = str(v1)+": max "+str(b)+" min "+str(a)
		archivo.write(lineab+"\n")
	archivo.close()

crea_reporte(temp1)


