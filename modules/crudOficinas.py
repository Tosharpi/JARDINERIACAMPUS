import json
import requests
import os

def getAllDataOfice():
    peticion = requests.get("http://172.16.103.32:5005")
    data = peticion.json()
    return data

def postOficina():
    ofice={
        "codigo_oficina": input("Ingrrese el codigo de la oficina: "),
        "ciudad": input("Ingrrese ls ciudad de la oficina: "),
        "pais": input("Ingrrese el pais de la oficina: "),
        "region": input("Ingrrese el codigo de la oficina: "),
        "codigo_postal": input("Ingrrese el codigo postal de la oficina: "),
        "telefono": input("Ingrrese el telefono de la oficina: "),
        "linea_direccion1": input("Ingrese la direccion_1 de la oficina: "),
        "linea_direccion2": input("Ingrese la direccion_2 de la oficina: ")
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.32:5005",  headers=headers , data=json.dumps(ofice, indent=4))
    res = peticion.json()
    res["Mensaje"] = "oficina guardado"
    return [res]

def menuCrudOficina():
    while True:
        os.system("clear")
        print("""
        

    ___       __          _       _      __                                       
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                      
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                          
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                           
       __      __                    __        ____  _____      _                 
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                  


            0. Salir                                                                  
            1. Ingresar oficina nueva
            2. Eliminar oficina 
            
          
    """)

        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postOficina()
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break

