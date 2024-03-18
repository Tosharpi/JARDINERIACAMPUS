import json
import requests
import os
from datetime import datetime
from tabulate import tabulate


def getAllDataPedidos():
    
    peticion = requests.get("http://172.16.100.136:5007")
    data = peticion.json()
    return data

def getCodigoPedido(codigoPed):
    listPed =[]
    
    for val in getAllDataPedidos():
        if (val.get('codigo_pedido') == codigoPed):
            listPed.append({
            "codigo_pedido":val.get('codigo_pedido'),
            "codigo_cliente":val.get('codigo_cliente')
           })
    return listPed

def getEstadosPedido():
    estadosPedido = []
    for val in getAllDataPedidos():
        val.get("estado")
        estadosPedido.append(
            {
                "codigo_pedido":val.get("codigo_pedido"),
                "estado":val.get("estado")
            }
        )
    return estadosPedido


#devuelve un listado con el codigo de pedido,
#codigo de cliente, fecha esperada y 
#fecha de entrega de los pedidos que no han sido entregados a tiempo.

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for pedidos in getAllDataPedidos():
        if (pedidos.get("estado") == "Entregado" and pedidos.get("fecha_entrega") is None):
            pedidos["fecha_entrega"]= pedidos.get("fecha_esperada")
            
        if pedidos.get("estado") == "Entregado":

            date_1 = "/".join(pedidos.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(pedidos.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0 :
                pedidosEntregado.append({
                    "codigo_pedido": pedidos.get("codigo_pedido"),
                    "codigo_cliente": pedidos.get("codigo_cliente"),
                    "fecha_esperada": pedidos.get("fecha_esperada"),
                    "fecha_de_entrega": pedidos.get("fecha_entrega")
                })

    return pedidosEntregado


#devuelve un listado con el codigo pedido, codigo de cliente, fecha esperada y fecha de
#entrega de los pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fecha esperada

def getAllPedAntesFechaEsperada():
    pedidosAntesFechaEsperada = []
    for val in getAllDataPedidos():

        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") is None):
            val["fecha_entrega"]= val.get("fecha_esperada")
            
        if(val.get("estado") == "Entregado"):

            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2 :
                pedidosAntesFechaEsperada.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return pedidosAntesFechaEsperada


def getAllPedRechazadosEn2008():
    pedidosRechazadosEn2008 = []
    for val in getAllDataPedidos():
        if val.get("estado") == "Rechazado":
            if val.get("fecha_pedido")[0:4] == "2008" and val.get("fecha_esperada")[0:4] == "2008":
                pedidosRechazadosEn2008.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "estado": val.get("estado"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return pedidosRechazadosEn2008


def getAllPedEntEnero():
    AllPedEntEnero = []
    for val in getAllDataPedidos():

        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") is None):
            val["fecha_entrega"]= val.get("fecha_esperada")

        if val.get("estado") == "Entregado":

            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
        
             
            if start.month == 1  :
                AllPedEntEnero.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return AllPedEntEnero

def menuReportesPedidos():
    while True:
        os.system("clear")
        print(""" 


                MENU DE PEDIDOS

            0. Salir                                                                                                        
            1. El codigo del cliente segun el pedido (cod pedido)
            2. Obtener el estado de todos los pedidos
            3. Informacion de pedidos que no han sido entregados a tiempo 
            4. Informacion de pedidos entregados dos dias (o mas) antes de la fecha de entrega
            5. Obtener los pedidos rechazados en el 2008
            6. Obtener los pedidos entregados en enero de cualquier mes
            
    """)
        
        opcion = int(input("Seleccione una de las opciones: "))

        if(opcion == 1):
            codigoPed = int(input('Ingrese el codigo del pedido: '))
            print(tabulate(getCodigoPedido(codigoPed), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 2):
            print(tabulate(getEstadosPedido(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 3):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 4):
            print(tabulate(getAllPedAntesFechaEsperada(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 5):
            print(tabulate(getAllPedRechazadosEn2008(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 6):
            print(tabulate(getAllPedEntEnero(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif(opcion == 0):
            break
