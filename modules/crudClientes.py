import json
import requests
import os
import re
from tabulate import tabulate

def getAllDataClient():

    peticion = requests.get("http://172.16.103.32:5003")
    data = peticion.json()
    return data

def getCodClient(id):
    peticion = requests.get(f"http://172.16.103.32:5003/clientes/{id}")
    return [peticion.json()] if peticion.ok else[]

def postCliente():
    cliente ={}
    while True:
        try:
            if not cliente.get("codigo_cliente"):
                
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r"^[0-9]{1,10}$", codigo) is not None):
                    datas = getCodClient(codigo)
                    if datas:
                        print(tabulate(datas, headers="keys", tablefmt="github"))
                        raise Exception("el codigo del cliente ya existe")
                    else:
                        codigo = int(codigo)
                        cliente["codigo_cliente"] = codigo
                else: 
                    raise Exception("el codigo  del producto no cumple con el estandar establecido")
            if not cliente.get("nombre_cliente"):
                
                nombre = input("Ingrese el nombre del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z\s]+(\s[A-Z][a-zA-Z\s]+)*$", nombre) is not None):
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception ("el nombre del cliente no cumple con los parametros")
            if not cliente.get("nombre_contacto"):
                
                nombre_contacto = input("Ingrese el nombre de contacto del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z\s]+(\s[A-Z][a-zA-Z\s]+)*$", nombre_contacto) is not None):
                    cliente["nombre_contacto"] = nombre_contacto
                else:
                    raise Exception ("el nombre de contacto del cliente no cumple con los parametros")
            if not cliente.get("apellido_contacto"):
                
                apellido_contacto = input("Ingrese el apellido del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z\s]+(\s[A-Z][a-zA-Z\s]+)*$", apellido_contacto) is not None):
                    cliente["apellido_contacto"] = apellido_contacto
                else:
                    raise Exception ("el apellido de contacto del cliente no cumple con los parametros")
            if not cliente.get("telefono"):
                
                telefono = input("Ingrese el telefono del cliente: ")
                if(re.match(r"^[0-9\s-]+$", telefono) is not None):
                    cliente["telefono"] = telefono
                else:
                    raise Exception ("el telefono de contacto del cliente no cumple con los parametros")
            if not cliente.get("fax"):
                
                fax = input("Ingrese el fax del cliente: ")
                if(re.match(r"^[0-9\s-]+$", fax) is not None):
                    cliente["fax"] = fax
                else:
                    raise Exception ("el fax de contacto del cliente no cumple con los parametros")
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input("Ingrese la direccion 1 del cliente: ")
                cliente["linea_direccion1"] = linea_direccion1
            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input("Ingrese la direccion 2 del cliente: ")
                cliente["linea_direccion2"] = linea_direccion2
            if not cliente.get("ciudad"):
                
                ciudad = input("Ingrese la ciudad del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", ciudad) is not None):
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception ("la ciudad del cliente no cumple con los parametros")
            if not cliente.get("region"):
                
                region = input("Ingrese la region del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", region) is not None):
                    cliente["region"] = region
                else:
                    raise Exception ("la region del cliente no cumple con los parametros")
            if not cliente.get("pais"):
                
                pais = input("Ingrese el pais del cliente: ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", pais) is not None):
                    cliente["pais"] = pais
                else:
                    raise Exception ("el pais del cliente no cumple con los parametros")
            if not cliente.get("codigo_postal"):
                
                codigo_postal = input("Ingrese el codigo postal del cliente: ")
                if(re.match(r"^[0-9]+$", codigo_postal) is not None):
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception ("el codigo postal del cliente no cumple con los parametros")
            if not cliente.get("codigo_empleado_rep_ventas"):
                
                codigo_empleado_rep_ventas = input("Ingrese el codigo del empleado R.V. del cliente: ")
                if(re.match(r"^[0-9]+$", codigo_empleado_rep_ventas) is not None):
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception ("el codigo del empleado R.V. del cliente no cumple con los parametros")
            if not cliente.get("limite_credito"):
                
                limite_credito = input("Ingrese el limite de credito del cliente: ")
                if(re.match(r"^[0-9]+$", limite_credito) is not None):
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception ("el limite de credito del cliente no cumple con los parametros")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.32:5003/clientes",  headers=headers , data=json.dumps(cliente, indent=4))
    res = peticion.json()
    tablaCliente = [cliente]
    print(tabulate(tablaCliente, headers="keys", tablefmt="github"))

def deletClient(id):
    data = getCodClient(id)
    if (len(data)):
        peticion = requests.delete(f"http://172.16.103.32:5003/clientes/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "el producto fue eliminado correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "producto no encontrado",
                    "data" : id
                },
                "status" : 400
}]

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
        if opcion ==2:
            id = input('Ingrese el id: ')
            print(tabulate(deletClient(id)["body"], headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break
