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

            if (region != None and val.get('region')):
                clientZone.append(val)
            elif (val.get('region') == None):
                clientZone.append(val)

    return clientZone