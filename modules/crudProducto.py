
import json
import requests
import os
import re
from tabulate import tabulate

def getAllDataProd():

    peticion = requests.get("http://172.16.100.136:5001")
    data = peticion.json()
    return data

def postProduct():
    producto={}
    while True:

        try:
            if not producto.get("codigo_producto"):

                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                    data = getCrudCodigoProd(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("el codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception ("el codigo  del producto no cumple con el estandar establecido")
                
            if(not producto.get("nombre")):

                nombre = input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$', nombre) is not None):
                    producto["nombre"] = nombre
                    break
                else:
                    raise Exception ("el nombre del producto no cumple con el estandar establecido")
            # if(not producto.get("gama")):
            #     gama = input("Ingrese la gama del producto: ")

            if not producto.get("dimensiones") is not None:

                dimensiones = input("Ingrese las dimensiones: ")
                if re.match(r'^[0-9]{1,5}x[0-9]{1,5}$', dimensiones):
                    print('algo')

        except Exception as error:
            print(error)
    print(producto)


def getCrudCodigoProd(codigo):
    for val in getAllDataProd():
        if(val.get("codigo_producto") == codigo):
            data = val
    return [data]
    

# producto = {
#             "codigo_producto": input("Ingrese el codigo del producto: "),
#             "nombre": input("Ingrese el nombre del producto: "),
#             "gama": input("Ingrese la gama del producto: "),
#             "dimensiones": input("Ingrese las dimensiones del producto: "),
#             "proveedor": input("Ingrese el proveedor del producto: "),
#             "descripcion": input("Ingrese la descripsion del producto: "),
#             "cantidad_en_stock": int(input("Ingrese el stock del producto: ")),
#             "precio_venta": int(input("Ingrese el precio del producto: ")),
#             "precio_proveedor": int(input("Ingrese el precio de proveedor del producto: "))
#         }
# headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
# peticion = requests.post("http://172.16.100.136:5001",  headers=headers , data=json.dumps(producto, indent=4))
# res = peticion.json()
# res["Mensaje"] = "Producto guardado"
# return [res]



def menuCrudProduct():
    while True:
        os.system("clear")
        print("""
        

    ___       __          _       _      __                                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                                   
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                                   
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                                       
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                                        
       __      __                    __        ____                 __           __            
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                               


            0. Salir                                                                  
            1. Ingresar producto nuevo
            2. Eliminar producto 
            
          
    """)


        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postProduct()
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break
