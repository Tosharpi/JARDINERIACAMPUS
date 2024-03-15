import json 
import requests
import os

def getAllDataEmpl():
    
    peticion = requests.get("http://172.16.100.136:5004")
    data = peticion.json()
    return data

def postEmpl():
    empl={
        "codigo_empleado": int(input("Ingrese el codigo del empleado: ")),
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese el apellido_1 del empleado: "),
        "apellido2": input("Ingrese el apellido_2 del empleado: "),
        "extension": input("Ingrese laextension  del empleado: "),
        "email": input("Ingrese el email del empleado: "),
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "codigo_jefe": int(input("Ingrese el codigo del jefe: ")) or None,
        "puesto": input("Ingrese el puesto del empleado: ")
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.100.136:5004",  headers=headers , data=json.dumps(empl, indent=4))
    res = peticion.json()
    res["Mensaje"] = "empleado guardado"
    return [res]

def menuCrudEmpl():
    while True:
        os.system("clear")
        print("""
        
    ___       __          _       _      __                                                       
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                                      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                                      
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                                          
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                                           
       __      __                    __        ______                __               __          
  ____/ /___ _/ /_____  _____   ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                          /_/                                     

            0. Salir                                                                  
            1. Ingresar empleado nuevo
            2. Eliminar empleado 
            
          
    """)

    

        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postEmpl()
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break

