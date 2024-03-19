import json
import requests
import os
import re
from tabulate import tabulate

def getAllDataOfice():
    peticion = requests.get("http://172.16.100.136:5005/oficina")
    data = peticion.json()
    return data

def getIdOfice(id):
    peticion = requests.get(f"http://172.16.100.136:5005/oficina{id}")
    return [peticion.json()] if peticion.ok else[]

def getCodOfice(cod_oficina):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas?codigo_oficina={cod_oficina}")
    return [peticion.json()] if peticion.ok else[]

def deletOfice(id):
    data = getCodOfice(id)
    if (len(data)):
        peticion = requests.delete(f"http://172.16.100.136:5005/oficina/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "la oficina fue eliminada correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "oficina no encontrada",
                    "data" : id
                },
                "status" : 400
}]





def postOficina():
    oficina ={}
    while True:
        try:
            if not oficina.get("codigo_oficina"):
                
                cod_oficina = input("Ingrese el codigo de la oficina: ")
                if(re.match(r"^[0-9]{1,10}$", cod_oficina) is not None):
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
                if(re.match(r"^[0-9]{9}$", codigo_postal) is not None):
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

#     headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
#     peticion = requests.post("http://172.16.100.136:5005/oficina",  headers=headers , data=json.dumps(oficina, indent=4))
#     res = peticion.json()
#     tablaOficina = [oficina]
#     print(tabulate(tablaOficina, headers="keys", tablefmt="github"))


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
        # if opcion == 1:
        #     postOficina()
        #     input('Oprima una tecla para continuar: ')
        if opcion == 2:
            id = input("Ingrese la id de la oficina")
            print(tabulate(deletOfice(id)["body"], headers="keys", tablefmt="github"))
            input('Oprima una tecla para continuar: ')
        elif opcion == 0:
            break

