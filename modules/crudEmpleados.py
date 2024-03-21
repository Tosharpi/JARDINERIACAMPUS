import json 
import requests
import os
from tabulate import tabulate
import re

def getAllDataEmpl():
    
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getIdEmpl(id):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    return [peticion.json()] if peticion.ok else[]

def deletEmpl(id):
    data = getIdEmpl(id)
    if (len(data)):
        print(tabulate(data, headers="keys", tablefmt="github"))
        opcion = input("¿Desea eliminar el siguiente dato? (si/no)")
        if opcion == "si":
            peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
            if peticion.status_code == 204 or peticion.status_code == 200:
                
                return print("El empleado fue eliminado correctamente")
            else:
                return print ("El empleado no puedo ser eliminado")
        else:
            print("Revisa si el id del empleado deseado es el correcto")
    else:
        print("El empleado no pudo ser econtrado. Revisa el id")   

def postEmpl():
    print('Los datos no obligatorios se saltan digitando la tecla "n" mayuscula. (N)')
    empleado ={}
    conf = input("¿Estas seguro que quieres ingresar un nuevo dato? si/no ")
    if conf == "si":

        while True:
            try:
                if not empleado.get("codigo_empleado"):
                    
                    codigo = input("Ingrese el codigo del empleado: ")
                    if(re.match(r'^[0-9]+$', codigo) is not None):
                        datas = getIdEmpl(codigo)
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
                        codigo_jefe = int(codigo_jefe)
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

        for val in empleado:
            if empleado[val] == "N":  
                empleado[val] = None
        

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.post("http://154.38.171.54:5003/empleados",  headers=headers , data=json.dumps(empleado, indent=4))
        res = peticion.json()
        tablaEmpleado = [empleado]
        print(tabulate(tablaEmpleado, headers="keys", tablefmt="github"))
    else:
        print()

def updateEmpl(id):
    data = getIdEmpl(id)
    if (len(data)):
        while True:
            # os.system("clear")
            print(tabulate(data, headers="keys", tablefmt="github"))
            print("""
            Que datos desea actualizar:
            
            1. nombre
            2. apellido1
            3. apellido2
            4. extension
            5. email
            6. codigo_oficina
            7. codigo_jefe
            8. puesto
            
            99. guardar
            """)
            
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                cambio = input("Ingrese el nombre: ")
                if re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", cambio):
                                
                    dataMod = data[0]
                    dataMod['nombre'] = cambio
                else:
                    print("el nombre no cumple con los parametros: ")
            elif opcion == 2:
                cambio = input("Ingrese el napellido del empleado: ")
                if re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", cambio):
                                
                    dataMod = data[0]
                    dataMod['apellido1'] = cambio
                else:
                    print("el apellido no cumple con los parametros: ")
            elif opcion == 3:
                cambio = input("Ingrese el apellido 2: ")
                if re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", cambio):
                                
                    dataMod = data[0]
                    dataMod['apellido2'] = cambio
                else:
                    print("el apellido no cumple con los parametros: ")
            elif opcion == 4:
                cambio = input("Ingrese la extension del empleado: ")
                if re.match(r"^[0-9\s-]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['extension'] = cambio
                else:
                    print("la extension no cumple con los parametros: ")
            elif opcion == 5:
                cambio = input("Ingrese el email: ")
                dataMod = data[0]
                dataMod['email'] = cambio
            elif opcion == 6:
                cambio = input("Ingrese el codigo de oficina: ")
                if re.match(r"^[A-Z-]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['codigo_oficina'] = cambio
                else:
                    print("el codigo oficina no cumple con los parametros: ")
            elif opcion == 7:
                cambio = input("Ingrese el codigo jefe:  ")
                if re.match(r"^[0-9]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['codigo_jefe'] = cambio
                else:
                    print("el codigo jefe no cumple con los parametros: ")
            elif opcion == 8:
                cambio = input("Ingrese el puesto: ")
                dataMod = data[0]
                dataMod['puesto'] = cambio
            elif opcion == 99:
                peticion = requests.put(f"http://154.38.171.54:5003/empleados/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                res = peticion.json()
                print("Empleado actualizado satisfactoriamente")
                break   
    else: 
        print("El id no existe")


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
            3. Actualizar datos de un empleados
          
    """)

    

        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postEmpl()
            input('Oprima una tecla para continuar: ')
        elif opcion ==2:
            id = input('Ingrese el id: ')
            print(tabulate(deletEmpl(id), headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion ==3:
            id = input('Ingrese el id: ')
            print(tabulate(updateEmpl(id), headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break
