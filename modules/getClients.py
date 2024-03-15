import json
import os
import requests
from tabulate import tabulate
import modules.crudClientes as crudcli
import modules.crudEmpleados as crudEmpl


def getAllClientName():
    clienteName = []
    for val in crudcli.getAllDataClient():
        clienteName.append({
            "codigo_cliente": val.get("codigo_cliente"),
            "nombre_cliente": val.get("nombre_cliente")
        })

    return clienteName


def getOneClientCodigo(codigo):
    for val in crudcli.getAllDataClient():
        if (val.get('codigo_cliente') == codigo):
            return [{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }]


def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredito = list()
    for val in crudcli.getAllDataClient():
        if (val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredito.append({
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente'),
                "limite": val.get('limite_credito'),
                "ciudad": val.get('ciudad')
            })

    return clienteCredito


def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = list()
    for val in crudcli.getAllDataClient():

        if (val.get("pais") == pais):
            # print("algo")
            if (val.get("region") == region) or region == None and (val.get("ciudad") == ciudad) or ciudad == None:
                # print('algosss')
                clientZone.append({
                    "codigo": val.get("codigo_cliente"),
                    "pais": val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region")
                })

    return clientZone


def getNombreContacto(codigo):

    contacClient = []
    for val in crudcli.getAllDataClient():
        if (val.get('codigo_cliente') == codigo):

            contacClient.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_contacto": val.get('nombre_contacto'),
                "apellido_contacto": val.get('apellido_contacto')
            })

    return contacClient


def getClientesPais(pais):
    ClientesPais = []
    for val in crudcli.getAllDataClient():
        if (val.get("pais") == pais):
            ClientesPais.append(
                {
                    "codigo_cliente": {val.get("codigo_cliente")},
                    "nombre_cliente": {val.get("nombre_cliente")},
                    "pais": {val.get("pais")}
                }
            )
    return ClientesPais


def getCityEmploy(ciudad):
    clientCity = []
    for val in crudcli.getAllDataClient():
        if (val.get("ciudad")) == ciudad and (val.get("codigo_empleado_rep_ventas") == 11) or (val.get("codigo_empleado_rep_ventas") == 30):
            clientCity.append(
                {
                    "codigoCliente": val.get("codigo_cliente"),
                    "nombreCliente": val.get("nombre_cliente"),
                    "ciudad": val.get("ciudad"),
                    "representante_de_ventas": val.get("codigo_empleado_rep_ventas")
                }
            )
    return clientCity


def getAllClientRep():
    allClientRep = []
    for val in crudcli.getAllDataClient():
        for val2 in crudEmpl.getAllDataEmpl():
            if val.get("codigo_empleado_rep_ventas") == val2.get("codigo_empleado") and val2.get("puesto") == "Representante Ventas":
                allClientRep.append(
                    {
                        "nombre": val.get("nombre_cliente"),
                        "nombre_rep": val2.get("nombre"),
                        "apellido_rep": f"{val2.get('apellido1')}  {val2.get('apellido2')}"
                    }
                )
    return allClientRep


def menuClientesReportes():

    while True:
        os.system("clear")
        print("""


    ____                        __               ____          __              
   / __ \___  ____  ____  _____/ /____  _____   / __ \___     / /   ____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / / _ \   / /   / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /___/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/  /_____/\___/  /_____/\____/____/  
         _/_/_____            __                                               
        / ____/ (_)__  ____  / /____  _____                                    
       / /   / / / _ \/ __ \/ __/ _ \/ ___/                                    
      / /___/ / /  __/ / / / /_/  __(__  )                                     
      \____/_/_/\___/_/ /_/\__/\___/____/                                      
                                                                               

          0. Salir
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informacion de clientes según su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
          4. Obtener todos los clientes de un pais, una region y una ciudad (pais, region, ciudad)
          5. Obtener el nombre de contacto de un cliente (codigo del cliente)
          6. Obtener clientes segun el pais
          7. Obtener todos los clientes segun su ciudad y su representante de ventas
          8. Obtener todos los clientes y sus representantes de ventas

""")

        opcion = int(input("Seleccione una de las opciones: "))

        if opcion == 1:
            print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 2:
            codigo = int(input('Ingrese el codigo del cliente: '))
            print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 3:
            limiteCredit = float(input('Ingresa el limite del credito: '))
            ciudad = input('Ingresa la ciudad: ')
            print(tabulate(getAllClientCreditoCiudad(limiteCredit, ciudad), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 4:
            pais = input('Ingresa el pais: ')
            region = input('Ingresa la region: ') or None
            ciudad = input('Ingresa la ciudad: ') or None
            print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 5:
            codigo = int(input('Ingrese el codigo del cliente: '))
            print(tabulate(getNombreContacto(codigo),headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 6:
            pais = input('ingrese el pais: ')
            print(tabulate(getClientesPais(pais),headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 7:
            ciudad = input('Ingrese la ciudad: ')
            print(tabulate(getCityEmploy(ciudad),headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 8:
            print(tabulate(getAllClientRep(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 0:
            break
