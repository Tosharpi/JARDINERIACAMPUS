
import json
import requests

def postProducto():
    
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
    peticion = requests.post("http://172.16.100.136:5001", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return [res]

def menu():
    while True:
        print("""
        
    ___       __          _       _      __                                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                                   
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                                   
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                                       
/_/  |_\__,_/_/_/_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/             __           __            
  ____/ /___ _/ /_____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                          /_/                                                  

              """)
    