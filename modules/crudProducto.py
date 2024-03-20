
import json
import requests
import os
import re
from tabulate import tabulate
#
def getAllDataProd():

    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data

def getIdProd(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")  
    data = peticion.json
    return [data.json()] if len(data) else[]

def deleteProducto(id):
    data = getIdProd(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
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

def getCrudCodigoProd(codigo):
    for val in getAllDataProd():
        data = list()
        if(val.get("codigo_producto") == codigo):
            data.append(val)
    return data

def postProduct():
    producto={}
    while True:

        try:
            if not producto.get("codigo_producto"):

                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r"^[0-9]+$", codigo) is not None):
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
                producto["nombre"] = nombre
            elif not producto.get("gama"):
                
                gama = input("Ingrese la gama del producto: ")
                if gama == "Ornamentales" or gama == "Frutales" or gama == "Herramientas" or gama == "Aromáticas":
                    producto["gama"] = gama
                else:
                    raise Exception ("el nombre del producto no cumple con el estandar establecido")
            elif not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones: ")
                if (re.match(r"^[0-9,x/]+$", dimensiones)is not None):
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception ("las dimensiones del producto no cumplen con los parametros")
          # generame una expresion regular que valide un maximo de cuatro palabras, cada una que empiece con mayuscula o minuscula y permita espacios entre cada palabra, incluso que permita siglas, como por ejemplo "S.A"
            elif not producto.get("proveedor"):
                proveedor = input("Ingrese el proveedor: ")
                if (re.match(r'^[A-Za-z.]+$', proveedor) is not None):
                    producto["proveedor"] = proveedor
                else:
                    raise Exception ("el proveedor del producto no cumplen con los paarametros")                
            elif not producto.get("descripcion"):
                descripcion = input("Ingrese la descripcion: ")
                producto["descripcion"] = descripcion
# generame una expresion regular en donde valide solo numeros y que solo admita un limite de 4 numeros.
            
            elif not producto.get("cantidadEnStock"):
                cantidad_en_stock = input("Ingrese el stock: ")
                if (re.match(r"^[0-9]+$", cantidad_en_stock) is not None):
                    cantidad_en_stock = int(cantidad_en_stock)
                    producto["cantidad_en_stock"] = cantidad_en_stock
                    
                else:
                    raise Exception ("el stock del producto no cumplen con los paarametros")
            
# generame una expresion regular en donde valide solo numeros y que solo admita un limite de 4 numeros.
            elif not producto.get("precio_venta"):
                precio_venta = input("Ingrese el precio venta: ")
                if (re.match(r'^[0-9]+$', precio_venta) is not None):
                    precio_venta = int(precio_venta)
                    producto["precio_venta"] = precio_venta
                else:
                    raise Exception ("el precio de venta del producto no cumplen con los paarametros")           
            elif not producto.get("precio_proveedor"):
                precio_proveedor = input("Ingrese el precio proveedor: ")
                if (re.match(r'^[0-9]+$', precio_proveedor) is not None):
                    precio_proveedor = int(precio_proveedor)
                    producto["precio_proveedor"] = precio_proveedor
                    break
                else:
                    raise Exception ("el precio de venta del producto no cumplen con los parametros")     
        except Exception as error:
            print(error)
        
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos",  headers=headers , data=json.dumps(producto, indent=4))
    res = peticion.json()
    tablaProducto = [producto]
    return print(tabulate(tablaProducto, headers="keys", tablefmt="github"))

def getProdCod(codigoProd):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?codigo_producto={codigoProd.upper()}")
    data = peticion.json()
    return data

def uptdateProdNom(id, codigo):
    while True:
        if(codigo!=None):
            print('xd')
            producto = getCrudCodigoProd(codigo)
            if (len(producto)):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                opcion = int(input("Es el producto que desea actualizar: 1. si 2. no"))
                if opcion == "si":
                    producto = producto[0]
                    producto["nombre"] = input("Ingrese el nuevo nombre del producto: ")
                    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
                    peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", headers=headers , data=json.dumps(producto, indent=4))
                    print("producto actualizado")
                    break
                else:
                    codigo = None
            else:
                print(f"El producto {codigo} no existe ")
                codigo = None
        else:
            codigo = ("Ingrese el codigo del producto que desea actualizar: ")

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
            3. Actualizar producto
            
          
    """)


        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postProduct()
            input('Oprima una tecla para continuar: ')
        elif opcion == 2:
            idProducto = input('Ingrese el id del producto: ')
            print (tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 3:
            id = input('Ingrese el id: ')
            codigo = input('Ingrese el codigo del producto que desea actualizar: ')
            print (tabulate(uptdateProdNom(id, codigo), headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        
        elif opcion == 0:
            break
