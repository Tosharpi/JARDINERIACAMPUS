import storage.clientes as cli 
from tabulate import tabulate

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

def menu():
    print(""" 

    _______                                             __                                      __                  __                             ______   __  __                        __                         
    |       \                                           |  \                                    |  \                |  \                           /      \ |  \|  \                      |  \                        
    | $$$$$$$\  ______    ______    ______    ______   _| $$_     ______    _______         ____| $$  ______        | $$  ______    _______       |  $$$$$$\| $$ \$$  ______   _______   _| $$_     ______    _______ 
    | $$__| $$ /      \  /      \  /      \  /      \ |   $$ \   /      \  /       \       /      $$ /      \       | $$ /      \  /       \      | $$   \$$| $$|  \ /      \ |       \ |   $$ \   /      \  /       $
    | $$    $$|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$  |  $$$$$$\|  $$$$$$$      |  $$$$$$$|  $$$$$$\      | $$|  $$$$$$\|  $$$$$$$      | $$      | $$| $$|  $$$$$$\| $$$$$$$\ \$$$$$$  |  $$$$$$\|  $$$$$$$
    | $$$$$$$\| $$    $$| $$  | $$| $$  | $$| $$   \$$  | $$ __ | $$    $$ \$$    \       | $$  | $$| $$    $$      | $$| $$  | $$ \$$    \       | $$   __ | $$| $$| $$    $$| $$  | $$  | $$ __ | $$    $$ \$$    \ 
    | $$  | $$| $$$$$$$$| $$__/ $$| $$__/ $$| $$        | $$|  \| $$$$$$$$ _\$$$$$$\      | $$__| $$| $$$$$$$$      | $$| $$__/ $$ _\$$$$$$\      | $$__/  \| $$| $$| $$$$$$$$| $$  | $$  | $$|  \| $$$$$$$$ _\$$$$$$$
    | $$  | $$ \$$     \| $$    $$ \$$    $$| $$         \$$  $$ \$$     \|       $$       \$$    $$ \$$     \      | $$ \$$    $$|       $$       \$$    $$| $$| $$ \$$     \| $$  | $$   \$$  $$ \$$     \|       $$
    \$$   \$$  \$$$$$$$| $$$$$$$   \$$$$$$  \$$          \$$$$   \$$$$$$$ \$$$$$$$         \$$$$$$$  \$$$$$$$       \$$  \$$$$$$  \$$$$$$$         \$$$$$$  \$$ \$$  \$$$$$$$ \$$   \$$    \$$$$   \$$$$$$$ \$$$$$$$ 
                        | $$                                                                                                                                                                                          
                        | $$                                                                                                                                                                                          
                        \$$                                                                                                                                                                                          

          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
          4. Obtener todos los clientes de un pais, una region y una ciudad (pais, region, ciudad)
          5. Obtener el nombre de contacto de un cliente (codigo del cliente)
          6. Obtener clientes españoles
""")

    opcion = int(input("Seleccione una de las opciones: "))

    if(opcion == 1):

        print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
        codigo = int(input('Ingrese el codigo del cliente: '))
        print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
    
