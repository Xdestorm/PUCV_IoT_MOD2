#producto mas caro
dato = ''
def producto_mas_caro (dato):
    from supermercado_c4 import productos
    mayor = -1
    for cod, nombre, precio, cant in productos:
        if precio > mayor:
            mayor = precio
            nombre_mayor = nombre
    return(nombre_mayor)

def valor_total_bodega(dato):
    from supermercado_c4 import productos
    suma = 0
    for cod, nombre, precio, cant in productos:
        suma += precio * cant
    return(suma)


def ingreso_total_por_ventas(dato):
    from supermercado_c4 import itemes, productos
    suma = 0
    for num_boleta, id_producto, cantidad in itemes:
        iditems = id_producto
        cantitems = cantidad
        for id_producto, nombre, precio, cantidad_bodega in productos:
            if iditems == id_producto:

                suma += precio * cantitems
    return(suma)

#programa
print(producto_mas_caro(dato))
print(valor_total_bodega(dato))
print(ingreso_total_por_ventas(dato))