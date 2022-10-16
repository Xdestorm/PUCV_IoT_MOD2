puntaje = int(input('ingrese puntaje:'))
d1 = 1
combinaciones = 0
while d1 <= 6:
    d2 = 1
    while  d2 <= 6:
        if d1 + d2 == puntaje:
            combinaciones +=1
        d2 +=1
    d1 += 1
print('hay',combinaciones, 'combinaciones para obtener',puntaje)
