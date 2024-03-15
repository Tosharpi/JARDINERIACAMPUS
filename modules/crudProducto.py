
import json
import requests
import os

def postProduct():
    
    producto = {
                "codigo_producto": input("Ingrese el codigo del producto: "),
                "nombre": input("Ingrese el nombre del producto: "),
                "gama": input("Ingrese la gama del producto: "),
                "dimensiones": input("Ingrese las dimensiones del producto: "),
                "proveedor": input("Ingrese el proveedor del producto: "),
                "descripcion": input("Ingrese la descripsion del producto: "),
                "cantidad_en_stock": int(input("Ingrese el stock del producto: ")),
                "precio_venta": int(input("Ingrese el precio del producto: ")),
                "precio_proveedor": int(input("Ingrese el precio de proveedor del producto: "))
            }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.33:5001",  headers=headers , data=json.dumps(producto, indent=4))
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return [res]

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
