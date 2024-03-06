import storage.oficina as of 
#Devuelve un listado
#oficina y la ciudad

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina" : val.get("codigo_oficina"),
            "ciudad" : val.get("ciudad")
        })
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono
#de las oficinas de españa

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais")==pais):

            ciudadTelefono.append({
                "ciudad" : val.get("ciudad"),
                "telefono" : val.get("telefono"),
                "oficina" : val.get("codigo_oficina"),
                "pais" : val.get("pais")
            })
    return ciudadTelefono



