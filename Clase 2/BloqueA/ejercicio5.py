i = 0
contador = 0
n = int(input('ingrese n: '))
while i < n:
    num = int(input())
    if num % 2 != 0:
        contador +=1
    i += 1
print('los impares son: ', contador)