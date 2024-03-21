import re
import os
import requests
import json
from tabulate import tabulate
import modules.getClients as client
import modules.crudClientes as crudClient
import modules.getOficina as oficina
import modules.crudOficinas as crudOfice
import modules.getEmpleado as empl
import modules.crudEmpleados as crudEmpl
import modules.getPedido as ped
import modules.crudPedidos as crudPed
import modules.getPago as pag
import modules.crudPago as crudPago
import modules.getProducto as prod
import modules.crudProducto as crudProd

def menuPrincipal():

        print("""
                
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                


                    1. Cliente
                    2. Oficina
                    3. Empleado
                    4. Pedido
                    5. Pago
                    6. Poductos
                    0. Salir
    """)

def menusClient():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/_________            __                                                                              
            / ____/ (_)__  ____  / /____  _____                                                                   
           / /   / / / _ \/ __ \/ __/ _ \/ ___/                                                                   
          / /___/ / /  __/ / / / /_/  __(__  )                                                                    
          \____/_/_/\___/_/ /_/\__/\___/____/                                                                     
                                                                                                                  

            0. Salir
            1. Reportes
            2. Administrar Clientes
          
""")

def menusOficinas():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/__  _____      _                                                                                     
          / __ \/ __(_)____(_)___  ____ ______                                                                    
         / / / / /_/ / ___/ / __ \/ __ `/ ___/                                                                    
        / /_/ / __/ / /__/ / / / / /_/ (__  )                                                                     
        \____/_/ /_/\___/_/_/ /_/\__,_/____/                                                                      

          
            0. Salir
            1. Reportes
            2. Administrar Oficinas

    """)

def menusEmpleados():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/____                __               __                                                              
          / ____/___ ___  ____  / /__  ____ _____/ /___  _____                                                    
         / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/                                                    
        / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )                                                     
       /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/                                                      
                      /_/                                                                                         

          
            0. Salir
            1. Reportes
            2. Administrar Empleados
    """)

def menusPedidos():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/__           ___     __                                                                              
          / __ \___  ____/ (_)___/ /___  _____                                                                    
         / /_/ / _ \/ __  / / __  / __ \/ ___/                                                                    
        / ____/  __/ /_/ / / /_/ / /_/ (__  )                                                                     
       /_/    \___/\__,_/_/\__,_/\____/____/                                                                      

                                                                                                       
            0. Salir
            1. Reportes
            2. Administrar pedidos
          
""")

def menusPagos():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/__                                                                                                   
          / __ \____ _____ _____  _____                                                                           
         / /_/ / __ `/ __ `/ __ \/ ___/                                                                           
        / ____/ /_/ / /_/ / /_/ (__  )                                                                            
       /_/    \__,_/\__, /\____/____/                                                                             
                   /____/                                                                                         

            0. Salir
            1. Reportes
            2. Administrar pagos
          
""")

def menusProductos():
    print("""

    ____                        __               ____     ___       __          _       _      __                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / /  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /    
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/  /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     
          /_/__                 __      __                                                                        
          / __ \_________  ____/ /_  __/ /_____  _____                                                            
         / /_/ / ___/ __ \/ __  / / / / __/ __ \/ ___/                                                            
        / ____/ /  / /_/ / /_/ / /_/ / /_/ /_/ (__  )                                                             
       /_/   /_/   \____/\__,_/\__,_/\__/\____/____/                                                              
                                                                                                                  
            0. Salir
            1. Reportes
            2. Administrar productos
          
""")

if __name__ == "__main__":

    while True:
        os.system("clear")
        
        menuPrincipal()
        

        opcion = input("Seleccione una de las opciones: ")
        
        #   toca importar "re"
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion == 1):
                while True:
                    os.system("clear")
                    menusClient()
                    opcion = int(input("Seleccione una de las opciones: "))

                    if opcion == 1:
                        client.menuClientesReportes()
                    elif opcion == 2:
                        crudClient.menuCrudClientes()
                    elif opcion == 0:
                        break

            elif(opcion == 2):
                while True:
                    os.system("clear")
                    menusOficinas()
                    opcion = int(input("Seleccione una de las opciones: "))
                    if opcion == 1:
                        oficina.menuReportesOficinas()
                    elif opcion == 2:
                        crudOfice.menuCrudOficina()
                    elif opcion == 0:
                        break

            elif(opcion == 3):
                while True:
                    os.system("clear")
                    menusEmpleados()
                    opcion = int(input("Seleccione una de las opciones: "))
                    if opcion == 1:
                        empl.menuReportesEmpl()
                    elif opcion == 2:
                        crudEmpl.menuCrudEmpl()
                    elif opcion == 0:
                        break

            elif(opcion == 4):
                while True:
                    os.system("clear")
                    menusPedidos()
                    opcion = int(input("Seleccione una de las opciones: "))
                    if opcion == 1:
                        ped.menuReportesPedidos()
                    elif opcion == 2:
                        crudPed.menuCrudPedidos()
                    elif opcion == 0:
                        break

            elif(opcion == 5):
                while True:
                    os.system("clear")
                    menusPagos()
                    opcion = int(input("Seleccione una de las opciones: "))
                    if opcion == 1:
                        pag.menuReportesPago()
                    elif opcion == 2:
                        crudPago.menuCrudPagos()
                    elif opcion == 0:
                        break

            elif(opcion == 6):
                while True:
                    os.system("clear")
                    menusProductos()
                    opcion = int(input("Seleccione una de las opciones: "))
                    if opcion == 1:
                        prod.menuReportesProduct()
                    elif opcion == 2:
                        crudProd.menuCrudProduct()
                    elif opcion == 0:
                        break

            elif(opcion == 0):
                break


    # with open("storage/pedido.json", "r") as f:
    #     fichero = f.read()
    #     data = json.loads(fichero)
    #     for i, val in enumerate(data):
    #         data[i]["id"] = (i+1)
    #     data = json.dumps(data, indent=4).encode("utf-8")
    # with open("storage/pedido.json", "wb+") as f1:
    #     f1.write(data)
    #     f1.close()
