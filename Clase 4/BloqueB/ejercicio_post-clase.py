#producto mas caro

def producto_con_mas_ingresos(itemes, productos):
     from supermercado_c4 import itemes, productos
     mayor = -1
     id_mayor = 0
     nom = ''
     
     for num_boleta, id_producto, cantidad in itemes:
        cantitems = cantidad
        if id_producto == id_producto:
            cantitems += cantidad
        if cantitems > mayor:
            mayor = cantitems
            id_mayor = id_producto
            for id_producto, nombre, precio, cantidad_bodega in productos:
                if id_mayor == id_producto:
                    nom = nombre
        return(nom)

def cliente_que_mas_pago(itemes, productos, clientes):
    from supermercado_c4 import itemes, productos, clientes

    


def ingreso_total_por_ventas(itemes, productos):
    from supermercado_c4 import itemes, productos



#programa
dato =''
producto_con_mas_ingresos(dato, dato)
ingreso_total_por_ventas(dato, dato)