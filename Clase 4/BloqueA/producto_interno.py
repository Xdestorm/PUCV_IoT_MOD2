def producto_interno(a, b):
    import numpy as np
    resultado = np.inner(a, b)
    print(resultado)
    return(resultado)

def son_ortogonales(a, b):
    resultado = producto_interno(a, b)
    if  resultado == 0:
        print('Son Ortorgonales')
    else:
        print('No son Ortogonales')