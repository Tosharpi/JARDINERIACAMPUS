import json
import requests
import os

def getAllDataPedidos():
    
    peticion = requests.get("http://172.16.103.33:5007")
    data = peticion.json()
    return data

def menuCrudPedidos():
    while True:
        os.system("clear")
        print("""
        

    ___       __          _       _      __                                       
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                      
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                          
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                           
       __      __                    __        ____           ___     __          
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \___  ____/ (_)___/ /___  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/  
                                                                                  


            0. Salir                                                                  
            1. Ingresar pedido nuevo
            2. Eliminar pedido
          
    """)

        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            print('en desarrollo')
        elif opcion == 0:
            break

