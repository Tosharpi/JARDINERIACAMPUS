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
            clienteCredito.append({
               "codigo": val.get('codigo_cliente'),
               "nombre": val.get('nombre_cliente'),
               "limite": val.get('limite_credito'),
               "ciudad": val.get('ciudad')
            })
        
    return clienteCredito

def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = list()
    for val in cli.clientes:
        
        if (val.get("pais") == pais):
            #print("algo")
            if (val.get("region") == region) or region == None and (val.get("ciudad") == ciudad) or ciudad == None:
                #print('algosss')            
                clientZone.append({
                "codigo":val.get("codigo_cliente"),
                "pais":val.get("pais"),
                "ciudad":val.get("ciudad"),
                "region":val.get("region")
                })
                
    return clientZone

def getNombreContacto(codigo):

    contacClient=[]
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
           
           contacClient.append({
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_contacto":{val.get('nombre_contacto')},
            "apellido_contacto":{val.get('apellido_contacto')}
           })
           
    return contacClient

def getClientesPais(pais):
    ClientesPais=[]
    for val in cli.clientes:
       if(val.get("pais") == pais):
           ClientesPais.append(
               {
                   "codigo_cliente":{val.get("codigo_cliente")},
                   "nombre_cliente":{val.get("nombre_cliente")},
                   "pais": {val.get("pais")}
               }
           )
    return ClientesPais

def menu():

    while True:
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

          0. Salir
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informacion de clientes según su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
          4. Obtener todos los clientes de un pais, una region y una ciudad (pais, region, ciudad)
          5. Obtener el nombre de contacto de un cliente (codigo del cliente)
          6. Obtener clientes segun el pais
            
""")

        opcion = int(input("Seleccione una de las opciones: "))

        if(opcion == 1):

            print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            codigo = int(input('Ingrese el codigo del cliente: '))
            print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            limiteCredit = float(input('Ingresa el limite del credito: '))
            ciudad = input('Ingresa la ciudad: ')
            print(tabulate(getAllClientCreditoCiudad(limiteCredit, ciudad), headers="keys", tablefmt="github"))
        elif(opcion == 4):
            pais = input('Ingresa el pais: ') 
            region = input('Ingresa la region: ') or None
            ciudad = input('Ingresa la ciudad: ') or None
            print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="github"))
        elif(opcion == 5):
            codigo = int(input('Ingrese el codigo del cliente: '))
            print(tabulate(getNombreContacto(codigo), headers="keys", tablefmt="github"))
        elif(opcion == 6):
            pais = input('ingrese el pais: ')
            print(tabulate(getClientesPais(pais), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break
