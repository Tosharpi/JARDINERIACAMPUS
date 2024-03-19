
import json
import requests
import os
import re
from tabulate import tabulate
import modules.getProducto as gT

def getAllDataProd():

    peticion = requests.get("http://172.16.103.32:5001")
    data = peticion.json()
    return data

def getCrudCodigoProd(codigo):
    for val in getAllDataProd():
        data = list()
        if(val.get("codigo_producto") == codigo):
            data.append(val)
    return data

def deleteProducto(idProducto):
    data = gT.getCodProd(idProducto)
    if (len(data)):
        peticion = requests.delete(f"http://172.16.103.32:5001/productos/{idProducto}")
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
                    "data" : idProducto
                },
                "status" : 400
            }]


def postProduct():
    producto={}
    while True:

        try:
            if not producto.get("codigo_producto"):

                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                    datas = getCrudCodigoProd(codigo)
                    if(datas):
                        print(tabulate(datas, headers="keys", tablefmt="github"))
                        raise Exception("el codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception ("el codigo  del producto no cumple con el estandar establecido")

            elif not producto.get("nombre"):

                nombre = input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$', nombre) is not None):
                    producto["nombre"] = nombre
                else:
                    raise Exception ("el nombre del producto no cumple con el estandar establecido")

            elif not producto.get("gama"):
                
                gama = input("Ingrese la gama del producto: ")
                if gama == "Ornamentales" or gama == "Frutales" or gama == "Herramientas" or gama == "Aromáticas":
                    producto["gama"] = gama
                else:
                    raise Exception ("el nombre del producto no cumple con el estandar establecido")
# generame una expresion regular que valide una cadena de maximo 5 numeros al inicio, luego valide una "x" y por ultimo que valide otra cadena de maximo 5 numeros. la "x" debe de estar en medio de los numeros iniciales y los finales.
# en python
            elif not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones: ")
                if (re.match(r'^[0-9]{1,5}x[0-9]{1,5}$', dimensiones)is not None):
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception ("las dimensiones del producto no cumplen con los parametros")
            
            # generame una expresion regular que valide un maximo de cuatro palabras, cada una que empiece con mayuscula o minuscula y permita espacios entre cada palabra, incluso que permita siglas, como por ejemplo "S.A"
            elif not producto.get("proveedor"):
                proveedor = input("Ingrese el proveedor: ")
                if (re.match(r'^[A-Za-z\s\.]+(?: [A-Za-z\s\.]+){0,3}$', proveedor) is not None):
                    producto["proveedor"] = proveedor
                else:
                    raise Exception ("el proveedor del producto no cumplen con los paarametros")
                
# generame una expresion regular que valide textos similares al siguiente: (ejemplo de descripcion de un producto)
                    
            elif not producto.get("descripcion"):
                descripcion = input("Ingrese la descripcion: ")
                producto["descripcion"] = descripcion
                if descripcion == None:
                    raise Exception ("la descripcion del producto no cumplen con los paarametros")

# generame una expresion regular en donde valide solo numeros y que solo admita un limite de 4 numeros.
            
            elif not producto.get("cantidad_en_stock"):
                cantidad_en_stock = input("Ingrese el stock: ")
                if (re.match(r'^[0-9]{1,4}$', cantidad_en_stock) is not None):
                    cantidad_en_stock = int(cantidad_en_stock)
                    producto["cantidad_en_stock"] = cantidad_en_stock
                    
                else:
                    raise Exception ("el stock del producto no cumplen con los paarametros")
            
# generame una expresion regular en donde valide solo numeros y que solo admita un limite de 4 numeros.
            elif not producto.get("precio_venta"):
                precio_venta = input("Ingrese el precio venta: ")
                if (re.match(r'^[0-9]{1,4}$', precio_venta) is not None):
                    precio_venta = int(precio_venta)
                    producto["precio_venta"] = precio_venta
                else:
                    raise Exception ("el precio de venta del producto no cumplen con los paarametros")
            
            elif not producto.get("precio_proveedor"):
                precio_proveedor = input("Ingrese el precio proveedor: ")
                if (re.match(r'^[0-9]{1,4}$', precio_proveedor) is not None):
                    precio_proveedor = int(precio_proveedor)
                    producto["precio_proveedor"] = precio_proveedor
                    break
                else:
                    raise Exception ("el precio de venta del producto no cumplen con los parametros")
        
        except Exception as error:
            print(error)
        
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.32:5001",  headers=headers , data=json.dumps(producto, indent=4))
    res = peticion.json()
    tablaProducto = [producto]
    return print(tabulate(tablaProducto, headers="keys", tablefmt="github"))


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
        elif opcion == 2:
            idProducto = input('Ingrese el id del producto: ')
            print (tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        
        elif opcion == 0:
            break
