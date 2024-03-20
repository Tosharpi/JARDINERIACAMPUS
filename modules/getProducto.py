import os
import json
import requests
from tabulate import tabulate

#:)

def getAllDataProduct():
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data

def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in getAllDataProduct():
        if(val.get("gama") == gama and val.get("cantidadEnStock") >= stock):
            condiciones.append(val)

    def price(val):

        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)

    for i, val in enumerate(condiciones):

        if(condiciones[i].get("descripcion")):
            condiciones[i]["descripcion"] = f'{val.get("descripcion")[:5]}...'
        
        condiciones[i] = {
            "codigo":val.get("codigo_producto"),
            "venta":val.get("precio_venta"),
            "nombre":val.get("nombre"),
            "gama":val.get("gama"),
            "dimensiones":val.get("dimensiones"),
            "proveedor":val.get("proveedor"),
            "descripcion":val.get("descripcion"),
            "stock":val.get("cantidadEnStock")
        }
    return condiciones

def getStockProduct(codProd):
    StockProduct = []
    for val in getAllDataProduct():
        if val.get("codigo_producto") == codProd:
            StockProduct.append({
            "codProd":val.get("codigo_producto"),
            "nombre":val.get("nombre"),
            "stock":val.get("cantidad_en_stock")
        })
        
    return StockProduct

def getAllProv():
    allProv=[]
    for val in getAllDataProduct():
        allProv.append({
            "codigo_producto": val.get("codigo_producto"),
            "nombre": val.get("nombre"),
            "proveedor": val.get("proveedor")
        })
    return allProv

def getProd(nombre_producto):
    prodList=[]
    for val in getAllDataProduct():
        if val.get("nombre") == nombre_producto:

            prodList.append({
                "codigo_prod":val.get("codigo_producto"),
                "nombre":val.get("nombre"),
                "precio":val.get("precio_venta"),
                "stock":val.get("cantidad_en_stock")
            })
    return prodList

def getCodProd(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")  
    return [peticion.json()] if peticion.ok else[]

def menuReportesProduct():

    while True:
        os.system("clear")
        print("""
            MENU  PRODUCTOS
              
            0. Para salir
            1. Obtener todos los productos segun su gama y su stock (gama, stock)
            2. Obtener el stock de un producto segun su codigo (codigo producto)
            3. Todos los productos y sus proveedores
            4. Buscar el precio y el stock de un producto por el nombre (nombre producto)
            5. Obtener el producto segun el id
        """)
        opcion = int(input("Seleccione una de las opciones: "))
        if opcion == 1:
            gama = input("Ingrese la gama: ")
            stock = int(input('ingrese el stock: '))
            print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 2:
            codProd = input('Ingrese el codigo del producto: ')
            print(tabulate(getStockProduct(codProd), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 3:
            print(tabulate(getAllProv(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 4:
            nombre_producto = input('Ingrese el nombre del producto: ')
            print(tabulate(getProd(nombre_producto), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 5:
            id = input('Ingrese el id del producto: ')
            print(tabulate(getCodProd(id), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif opcion == 0:
            break
            
