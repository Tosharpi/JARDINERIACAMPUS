import json
import requests
import os

def getAllDataClient():

    peticion = requests.get("http://172.16.103.39:5003")
    data = peticion.json()
    return data

def postCliente():
    
    cliente = {
                "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
                "nombre_cliente": input("Ingrese el nombre del cliente: "),
                "nombre_contacto": input("Ingrese el nombre de contacto del cliente: "),
                "apellido_contacto": input("Ingrese el apellido de contacto del cliente: "),
                "telefono": input("Ingrese el numero de telefono del cliente: "),
                "fax": input("Ingrese el fax del cliente: "),
                "linea_direccion1": input("Ingrese la direccion del cliente: "),
                "linea_direccion2": input("Ingrese la direccion 2 del cliente: ") or None,
                "ciudad": input("Ingrese la ciudad del cliente: "),
                "region": input("Ingrese la region del cliente: ") or None,
                "pais": input("Ingrese el pais del cliente: "),
                "codigo_postal": input("Ingrese el codigo postal del cliente: "),
                "codigo_empleado_rep_ventas": int(input("Ingrese el representante de ventas del cliente: ")),
                "limite_credito": int(input("Ingrese el limite de credito del cliente: "))
            }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.39:5003",  headers=headers , data=json.dumps(cliente, indent=4))
    res = peticion.json()
    res["Mensaje"] = "cliente guardado"
    return [res]


def menuCrudClientes():

    while True:
        os.system("clear")
        print("""
        
    ___       __          _       _      __                                     
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                    
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                    
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                        
/_/  |_\__,_/_/_/_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/            __           
  ____/ /___ _/ /_____  _____   ____/ /__     _____/ (_)__  ____  / /____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/  

            0. Salir                                                                  
            1. Ingresar cliente nuevo
            2. Eliminar cliente 
          
    """)


        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postCliente()
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break

