import storage.clientes as cli 

def getAllClientName():
    clienteName =list()
    for i, val in enumerate(cli.clientes):
        codigoName=dict({
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_cliente":{val.get('nombre_cliente')}
        })
        clienteName.append(codigoName)
        
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
           return {
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_cliente":{val.get('nombre_cliente')}
           }
        
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredito =list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredito.append(val)
        
    return clienteCredito

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        
        if (val.get('pais') == pais):
            
            if (val.get('region') == region) or region == None:
                
                if (val.get('ciudad') == ciudad) or ciudad == None:
                    
                    userInZone=dict({
                    "codigo_cliente":{val.get('codigo_cliente')},
                    "pais":{val.get('pais')},
                    "ciudad":{val.get('ciudad')},
                    "region":{val.get('region')}
                    })
                    clientZone.append(userInZone)                  
    return clientZone

def getNombreContacto(codigo):

    contacClient=[]
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
           
           usuarioContacto={
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_contacto":{val.get('nombre_contacto')},
            "apellido_contacto":{val.get('apellido_contacto')}
           }
           contacClient.append(usuarioContacto)
    return contacClient

def getClientesEspañoles(pais):
    getClientesEspañoles=[]
    for val in cli.clientes:
       if(val.get("pais") == "Spain"):
           getClientesEspañoles.append(
               {
                   "codigo_cliente":{val.get("codigo_cliente")},
                   "nombre_cliente":{val.get("nombre_cliente")},
                   "pais": {val.get("pais")}
               }
           )
    return getClientesEspañoles