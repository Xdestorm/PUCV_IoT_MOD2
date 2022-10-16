a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9) # x = (27,3) and y = 9
z, w = x # z = 27 and w = 3
v = (x, a)


print('01:', a < b) #compara la primera posicion de las listas (a,b)
print('02:', y + w) #
print('03:', x + a) # concatena los valores de x and a 
print('04:', len(v)) #
print('05:', v[1][1]) #trae datos de la lista y tuplas
print('06:', c[0]) #trae la pisicion 0
print('07:', a + b[1:5]) #trae todo a y solo de la 
print('08:', (a + b)[1:5]) # 
print('09:', str(a[2]) + str(b[2])) # 
print('10:', str(a[2] + b[2])) #
print('11:', str((a + b)[2])) #
print('12:', str(a + b)[2][0]) #