import json
import requests
import os
from tabulate import tabulate
import re
#
def getAllDataPago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data

def getCodPago():
    peticion = requests.get(f"http://154.38.171.54:5006/pagos")
    return [peticion.json()] if peticion.ok else[]

def getIdPago(id):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    return [peticion.json()] if peticion.ok else[]

def postPago():
    pago ={}
    while True:
        try:
            if not pago.get("id_transaccion"):
                
                id_transaccion= input("Ingrese la id de la transaccion:  ")
                if(re.match(r"^[a-z0-9-]+$", id_transaccion) is not None):
                    datas=getCodPago()
                    for val in datas:
                        
                        if val.get("id_transaccion") == id_transaccion:
                            print(tabulate(val, headers="keys", tablefmt="github"))
                            raise Exception("el codigo del empleado ya existe")
                        else:
                            pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception ("la id de la transaccion no cumple con los parametros")
            if not pago.get("codigo_cliente"):
                
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    codigo = int(codigo)
                    pago["codigo_cliente"] = codigo
                else:
                    raise Exception("el codigo del cliente no cumple con el estandar establecido")
            if not pago.get("forma_pago"):
                
                forma_pago = input("Ingrese la forma de pago: ")
                if(re.match(r"^[A-Za-z]+$", forma_pago) is not None):
                    pago["forma_pago"] = forma_pago
                else:
                    raise Exception ("la forma de pago no cumple con los parametros")
            if not pago.get("fecha_pago"):
                
                fecha_pago = input("Ingrese la fecha de pago: ")
                if(re.match(r"^[0-9-]+$", fecha_pago) is not None):
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception ("la fecha de pago no cumple con los parametros")
            if not pago.get("total"):
                
                total_pago = input("Ingrese el total del pago: ")
                if(re.match(r"^[0-9\s-]+$", total_pago) is not None):
                    pago["total"] = total_pago
                    break
                else:
                    raise Exception ("el total no cumple con los parametros")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos",  headers=headers , data=json.dumps(pago, indent=4))
    res = peticion.json()
    tablapago = [pago]
    print(tabulate(tablapago, headers="keys", tablefmt="github"))

def deletePago(id):
    data = getIdPago(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
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

def menuCrudPagos():
    while True:
        os.system("clear")
        print("""
        

    ___       __          _       _      __                                
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______               
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/               
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                   
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                    
       __      __                    __        ____                        
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \____ _____ _____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
                                                       /____/              


            0. Salir                                                                  
            1. Ingresar pago nuevo
            2. Eliminar pago
            
          
    """)


        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postPago()
            input('Oprima una tecla para continuar: ')
        elif opcion == 2:
            id = input('Ingrese el id: ')
            deletePago(id)
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break


