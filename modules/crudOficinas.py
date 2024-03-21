import json
import requests
import os
import re
from tabulate import tabulate
#
def getAllDataOfice():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data

def getIdOfice(id):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    return [peticion.json()] if peticion.ok else[]

def getCodOfice(cod_oficina):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas?codigo_oficina={cod_oficina}")
    return [peticion.json()] if peticion.ok else[]

def deletOfice(id):
    data = getCodOfice(id)
    if (len(data)):
        print(tabulate(data, headers="keys", tablefmt="github"))
        opcion = input("¿Desea eliminar el siguiente dato? (si/no)")
        if opcion == "si":
            peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
            if peticion.status_code == 204 or peticion.status_code == 200:

                return  print("El producto fue eliminado correctamente")
            else:
                return print ("El producto no puedo ser eliminado")
        else:
            print("Revisa si el id del producto deseado es el correcto")
    else:
        print("El producto no pudo ser econtrado. Revisa el id") 

def postOficina():
    print('Los datos no obligatorios se saltan digitando la tecla "n" mayuscula. (N)')
    oficina ={}
    conf = input("¿Estas seguro que quieres ingresar un nuevo dato? si/no ")
    if conf == "si":
        while True:
            try:
                if not oficina.get("codigo_oficina"):
                    
                    cod_oficina = input("Ingrese el codigo de la oficina: ")
                    if(re.match(r"^[A-Z-]+$", cod_oficina) is not None):
                        datas = getCodOfice(cod_oficina)
                        if datas:
                            print(tabulate(datas, headers="keys", tablefmt="github"))
                            raise Exception("el codigo de la oficina ya existe")
                        else:
                            codigo_oficina = input("el codigo de la oficina: ")
                            if (re.match(r"^[A-Z-]+$", codigo_oficina) is not None):
                                oficina["codigo_oficina"] = codigo_oficina
                    else: 
                        raise Exception("el codigo  de la oficina no cumple con el estandar establecido")
                if not oficina.get("ciudad"):
                    
                    ciudad = input("Ingrese la ciudad de la oficina: ")
                    if(re.match(r"^[A-Z][a-zA-Z]+$", ciudad) is not None):
                        ciudad["ciudad"] = ciudad
                    else:
                        raise Exception ("la ciudad de la oficina no cumple con los parametros")
                if not oficina.get("pais"):
                    
                    pais = input("Ingrese el pais de la oficina ")
                    if(re.match(r"^[A-Z][a-zA-Z]+$", pais) is not None):
                        oficina["pais"] = pais
                    else:
                        raise Exception ("el pais de la oficina no cumple con los parametros")
                if not oficina.get("region"):
                    
                    region = input("Ingrese la region de la oficina ")
                    if(re.match(r"^[A-Z][a-zA-Z]+$", region) is not None):
                        oficina["region"] = region
                    else:
                        raise Exception ("la region de la oficina no cumple con los parametros")
                if not oficina.get("codigo_postal"):
                    
                    codigo_postal = input("Ingrese el codigo postal de la oficina ")
                    if(re.match(r"^[0-9]+$", codigo_postal) is not None):
                        oficina["codigo_postal"] = codigo_postal
                    else:
                        raise Exception ("el telefono de contacto del cliente no cumple con los parametros")
                if not oficina.get("telefono"):
                    
                    telefono = input("Ingrese el telefono de la oficina ")
                    if(re.match(r"^[0-9\s-]+$", telefono) is not None):
                        oficina["telefono"] = telefono
                    else:
                        raise Exception ("el telefono de la oficina no cumple con los parametros")
                if not oficina.get("linea_direccion1"):
                    linea_direccion1 = input("Ingrese la direccion 1 del cliente: ")
                    oficina["linea_direccion1"] = linea_direccion1
                if not oficina.get("linea_direccion2"):
                    linea_direccion2 = input("Ingrese la direccion 2 del cliente: ")
                    oficina["linea_direccion2"] = linea_direccion2
                    break
            except Exception as error:
                print(error)

            for val in oficina:
                if oficina[val] == "N":  
                    oficina[val] = None

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.post("http://154.38.171.54:5005/oficinas",  headers=headers , data=json.dumps(oficina, indent=4))
        res = peticion.json()
        tablaOficina = [oficina]
        print(tabulate(tablaOficina, headers="keys", tablefmt="github"))
    else:
        print()


def updateOfice(id):
    data = getIdOfice(id)
    if (len(data)):
        while True:
            # os.system("clear")
            print(tabulate(data, headers="keys", tablefmt="github"))
            print("""
            Que datos desea actualizar:
            
            1. ciudad
            2. pais
            3. region
            4. codigo_postal
            5. telefono
            6. linea_direccion1
            7. linea_direccion2
                  
            99. guardar
            """)
            
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                cambio = input("Ingrese la ciudad de la oficina")
                if re.match(r"^[A-Z-]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['ciudad'] = cambio
                else:
                    print("el nombre no cumple con los parametros: ")
            elif opcion == 2:
                cambio = input("Ingrese el pais: ")
                if re.match(r"^[A-Z][a-zA-Z]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['pais'] = cambio
                else:
                    print("el pais no cumple con los parametros: ")
            elif opcion == 3:
                cambio = input("Ingrese la region: ")
                if re.match(r"^[A-Z][a-zA-Z]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['region'] = cambio
                else:
                    print("la region no cumple con los parametros: ")
            elif opcion == 4:
                cambio = input("Ingrese el codigo postal: ")
                if re.match(r"^[0-9]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['codigo_postal'] = cambio
                else:
                    print("el codigo postal no cumple con los parametros: ")
            elif opcion == 5:
                cambio = input("Ingrese el telefono: ")
                if re.match(r"^[0-9\s-]+$", cambio):
                                
                    dataMod = data[0]
                    dataMod['telefono'] = cambio
                else:
                    print("el telfono no cumple con los parametros: ")
            elif opcion == 6:
                cambio = input("Ingrese la linea direccion 1 del contacto del cliente: ")        
                dataMod = data[0]
                dataMod['linea_direccion1'] = cambio
            elif opcion == 7:
                cambio = input("Ingrese la linea direccion 2 del cliente: ")
                dataMod = data[0]
                dataMod['linea_direccion2'] = cambio
            
            elif opcion == 99:
                peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                res = peticion.json()
                print("la oficina fue actualizada satisfactoriamente")
                break   
    else: 
        print("El id no existe")


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
            3. Actualizar datos de un cliente
          
    """)

        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            postOficina()
            input('Oprima una tecla para continuar: ')
        if opcion == 2:
            id = input("Ingrese la id de la oficina")
            print(tabulate(deletOfice(id), headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        if opcion == 3:
            id = input('Ingrese la id del cliente a actualizar: ')
            print(tabulate(updateOfice(id), headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break

