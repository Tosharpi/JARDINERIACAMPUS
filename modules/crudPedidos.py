import json
import requests
import os
import re
from tabulate import tabulate

def getAllDataPedidos():
    
    peticion = requests.get("http://172.16.100.136:5007")
    data = peticion.json()
    return data

def getCrudCodigoPed(codigo):
    for val in getAllDataPedidos():
        data = list()
        if(val.get("codigo_pedido") == codigo):
            data.append(val)
    return data

def postPedido():
    pedido={}
    while True:

        try:
            if not pedido.get("codigo_pedido"):

                codigo = input("Ingrese el codigo del pedido: ")
                if(re.match(r'^[0-9]{1,4}$', codigo) is not None):
                    codigo = int(codigo)
                    datas = getCrudCodigoPed(codigo)
                    if(datas):
                        print(tabulate(datas, headers="keys", tablefmt="github"))
                        raise Exception("el codigo pedido ya existe")
                    else:
                        pedido["codigo_pedido"] = codigo
                else:
                    raise Exception ("el codigo  del producto no cumple con el estandar establecido")
                
            elif not pedido.get("fecha_pedido"):
# generame una expresion regular que valide cuatro primeros números, luego agregar un guion, luego dos numeros, agregar un guion y por ultimo que valide dos numeros al final. 
                fecha = input("Ingrese la fecha de pedido: ")
                if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha) is not None):
                    pedido["fecha_pedido"] = fecha
                else:
                    raise Exception ("la fecha del pedido no cumple con el estandar establecido")
            
            elif not pedido.get("fecha_esperada"):
                
                fecha_esperada = input("Ingrese la fecha esperada del pedido: ")
                if (re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha_esperada) is not None):
                    pedido["fecha_esperada"] = fecha_esperada
                else:
                    raise Exception ("la fecha  de llegada del pedido no cumple con el estandar establecido")

            elif not pedido.get("fecha_entrega"):
                fecha_entrega = input("Ingrese la fecha de entrega: ")
                if (re.match(r'^(?:[0-9]{4}-[0-9]{2}-[0-9]{2}|None)$', fecha_entrega)):
                    pedido["fecha_entrega"] = fecha_entrega
                else:
                    raise Exception ("La fecha de entrega no tiene el formato correcto. Debe ser YYYY-MM-DD.")
            
            elif not pedido.get("estado"):
# La siguiente expresión regular valida una palabra que comienza con una letra mayúscula y el resto de la palabra es minúscula:
                estado = input("Ingrese el estado: ")
                if (re.match(r'^[A-Z][a-z]+$', estado) is not None):
                    pedido["estado"] = estado
                else:
                    raise Exception ("el estado del producto no cumplen con los parametros")
                
                    
            elif not pedido.get("comentario"):
                comentario = input("Ingrese el comentario: ") is not None
                pedido["comentario"] = comentario

# generame una expresion regular en donde valide solo numeros y que solo admita un limite de 4 numeros.
            
            elif not pedido.get("codigo_cliente"):
                codigo_cliente = input("Ingrese el codigo del cliente: ")
                if (re.match(r'^[0-9]{1,4}$', codigo_cliente) is not None):
                    codigo_cliente = int(codigo_cliente)
                    pedido["codigo_cliente"] = codigo_cliente
                    break
                else:
                    raise Exception ("codigo del cliente no cumplen con los paarametros")

        except Exception as error:
            print(error)
        
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.100.136:5007",  headers=headers , data=json.dumps(pedido, indent=4))
    res = peticion.json()
    tablaPedido = [pedido]
    return print(tabulate(tablaPedido, headers="keys", tablefmt="github"))

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
            postPedido()
            input("Pata continuar oprima alguna tecla...")
        if opcion == 2:
            print('En desarrollo')
        elif opcion == 0:
            break

