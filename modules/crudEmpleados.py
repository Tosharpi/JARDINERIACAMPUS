import json 
import requests
import os
from tabulate import tabulate
import re

def getAllDataEmpl():
    
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getCodEmpl(id):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    return [peticion.json()] if peticion.ok else[]

def deletEmpl(id):
    data = getCodEmpl(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "el producto fue eliminado correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "producto no encontrado",
                    "data" : id
                },
                "status" : 400
}]

def postEmpl():
    empleado ={}
    while True:
        try:
            if not empleado.get("codigo_empleado"):
                
                codigo = input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    datas = getCodEmpl(codigo)
                    if datas:
                        print(tabulate(datas, headers="keys", tablefmt="github"))
                        raise Exception("el codigo del empleado ya existe")
                    else:
                        codigo = int(codigo)
                        empleado["codigo_empleado"] = codigo
                else: 
                    raise Exception("el codigo  del producto no cumple con el estandar establecido")
            if not empleado.get("nombre"):
                
                nombre = input("Ingrese el nombre del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", nombre) is not None):
                    empleado["nombre"] = nombre
                else:
                    raise Exception ("el nombre del empleado no cumple con los parametros")
            if not empleado.get("apellido1"):
                
                apellido_1= input("Ingrese el apellido 1 del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", apellido_1) is not None):
                    empleado["apellido1"] = apellido_1
                else:
                    raise Exception ("el apellido del empleado no cumple con los parametros")
            if not empleado.get("apellido2"):
                
                apellido_2 = input("Ingrese el apellido 2 del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", apellido_2) is not None):
                    empleado["apellido2"] = apellido_2
                else:
                    raise Exception ("el apellido del empleado no cumple con los parametros")
            if not empleado.get("extension"):
                
                extension = input("Ingrese la extension del empleado: ")
                if(re.match(r"^[0-9\s-]+$", extension) is not None):
                    empleado["extension"] = extension
                else:
                    raise Exception ("la extension del contacto del cliente no cumple con los parametros")
            if not empleado.get("email"):
                email = input("Ingrese el correo del empleado: ")
                empleado["email"] = email
            if not empleado.get("codigo_oficina"):
                codigo_oficina = input("Ingrese el codigo de la oficina del empleado: ")
                if(re.match(r"^[A-Z-]+$", codigo_oficina) is not None):
                    empleado["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception ("el codigo de oficina del empleado no cumple con los parametros")
            if not empleado.get("codigo_jefe"):
                codigo_jefe = input("Ingrese el codigo del jefe: ")
                if(re.match(r"^[0-9]+$", codigo_jefe) is not None):
                    empleado["codigo_jefe"] = codigo_jefe
                else:
                    raise Exception ("el codigo del jefe del empleado no cumple con los parametros: ")
            if not empleado.get("puesto"):
                puesto = input("Ingrese el puesto del empleado: ")
                if(re.match(r"^[A-Z][a-zA-Z\s]+$", puesto) is not None):
                    empleado["puesto"] = puesto
                    break
                else:
                    raise Exception ("el puesto del empleado no cumple con los parametros")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5003/empleados",  headers=headers , data=json.dumps(empleado, indent=4))
    res = peticion.json()
    tablaEmpleado = [empleado]
    print(tabulate(tablaEmpleado, headers="keys", tablefmt="github"))

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
        elif opcion ==2:
            id = input('Ingrese el id: ')
            print(tabulate(deletEmpl(id)["body"], headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break
