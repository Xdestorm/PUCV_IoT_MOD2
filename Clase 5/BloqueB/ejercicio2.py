paises= {
'Juan':{'Chile', 'Argentina'},
'Pedro': {'Francia', 'Suiza', 'Chile'},
'Diego': {'Chile', 'Italia', 'Francia', 'Peru'}
}


def cuantos_en_comun (nombre1, nombre2):
    valor = (nombre1 - nombre2)
    return(valor)
nom1 = 'Juan'
nom2 = 'Diego'
print(cuantos_en_comun(nom1, nom2))