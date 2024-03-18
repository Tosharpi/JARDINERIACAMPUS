import json
import requests
import os

def getAllDataPago():
    peticion = requests.get("http://172.16.100.136:5006")
    data = peticion.json()
    return data

def postPago():
    pago={
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese la id del pago: "),
        "fecha_pago": input("Ingrese la fecha del pago: "),
        "total": int(input("Ingrese el total del pago: "))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.100.136:5006",  headers=headers , data=json.dumps(pago, indent=4))
    res = peticion.json()
    res["Mensaje"] = "pago guardado"
    return [res]

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
        elif opcion == 0:
            break


