from tabulate import tabulate
import modules.crudEmpleados as crudEmpl
import os
# cevuelve un listado con el nombre, apellidos y email
# de los empleados  segun el codigo del jefe


def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []

    for val in crudEmpl.getAllDataEmpl():
        if(val.get("codigo_jefe") == codigo):
          
          nombreApellidoEmail.append(
             {
              "nombre": val.get("nombre"),
            "apellido": f"({val.get('apellido1')} {val.get('apellido2')})",
            "email": val.get("email"),
            "jefe": val.get("codigo_jefe")
             }
            )
             
    return nombreApellidoEmail


# devuelve el nombre del puesto, nombre, apellido y email del jefe de la empresa 

def getAllNombrePuestoNombreApellidoEmail():
    NombrePuestoNombreApellidoEmail = []
    for val in crudEmpl.getAllDataEmpl():
        if (val.get("codigo_jefe")) == None:
            NombrePuestoNombreApellidoEmail.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email")
            })
    return NombrePuestoNombreApellidoEmail

# devuelve un listado con el nombre, apellidos y puesto de aquellos empleados
# que no sean representantes de ventas

def getNoRepresentanteDeVentas():
    NoRepresentanteDeVentas=[]
    for val in crudEmpl.getAllDataEmpl():
        if(val.get("puesto") != "Representante Ventas"):
            NoRepresentanteDeVentas.append(
                {
                    "nombre": val.get("puesto"),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "puesto": val.get("puesto")
                }
            )
    return NoRepresentanteDeVentas

def menuReportesEmpl():
    while True:
        os.system("clear")
        print(""" 

    ____                        __               ______                __               __          
   / __ \___  ____  ____  _____/ /____  _____   / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                               /_/                                     
                                                           
                                                                                                                    
            1. Ver los empleados de cada jefe (codigo jefe)
            2. Informacion del jefe de la empresa
            3. Tener todos los empleados que no sean representantes de ventas

    """)
        
        opcion = int(input("Seleccione una de las opciones: "))

        if(opcion == 1):
            codigo = int(input('Ingrese el codigo del jefe: '))
            print(tabulate(getAllNombreApellidoEmailJefe(codigo), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 2):
            print(tabulate(getAllNombrePuestoNombreApellidoEmail(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 3):
            print(tabulate(getNoRepresentanteDeVentas(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 0):
            break