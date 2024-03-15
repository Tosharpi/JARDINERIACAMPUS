import json 
import requests
import os

def getAllDataEmpl():
    
    peticion = requests.get("http://172.16.103.33:5004")
    data = peticion.json()
    return data

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
            print('en desarrollo')
        elif opcion == 0:
            break

