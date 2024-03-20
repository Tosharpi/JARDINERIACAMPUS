import modules.crudOficinas as crudOfice
from tabulate import tabulate
import os
#Devuelve un listado
#oficina y la ciudad

#:)

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in crudOfice.getAllDataOfice():
        codigoCiudad.append({
            "codigo_oficina" : val.get("codigo_oficina"),
            "ciudad" : val.get("ciudad")
        })
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono
#de las oficinas

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in crudOfice.getAllDataOfice():
        if(val.get("pais")==pais):

            ciudadTelefono.append({
                "ciudad" : val.get("ciudad"),
                "telefono" : val.get("telefono"),
                "oficina" : val.get("codigo_oficina"),
                "pais" : val.get("pais")
            })
    return ciudadTelefono

def menuReportesOficinas():
    while True:
        os.system("clear")
        print(""" 

 __       __                                       ______    ______   __            __                               

    ____                        __               ____  _____      _                 
   / __ \___  ____  ____  _____/ /____  _____   / __ \/ __(_)____(_)___  ____ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
          /_/                                                                       
                                                                                                          
          0. Salir
          1. La oficina de cada ciudad
          2. La ciudad y el telefono de cada oficina segun el pais (pais)

    """)
        opcion = int(input('Seleccione la opcion: '))
        if (opcion == 1):
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 2):
            pais = input('Ingrese el país: ')
            print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 0):
            break


