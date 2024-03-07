import storage.pedido as ped 
from datetime import datetime


def getCodigoPedido(codigoPed):
    for val in ped.pedido:
        if (val.get('codigo_pedido') == codigoPed):
            return {
            "codigo_pedido":{val.get('codigo_pedido')},
            "codigo_cliente":{val.get('codigo_cliente')}
           }

def getEstadosPedido():
    estadosPedido = []
    for val in ped.pedido:
        val.get("estado")
        estadosPedido.append(
            {
                "codigo_pedido":{val.get("codigo_pedido")},
                "estado":{val.get("estado")}
            }
        )
    return estadosPedido


#devuelve un listado con el codigo de perdido,
#codigo de cliente, fecha esperada y 
#fecha de entrega de los pedidos que no han sido entregados a tiempo.

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for pedidos in ped.pedido:
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
    for val in ped.pedido:

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
    for val in ped.pedido:
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
    for val in ped.pedido:

        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") is None):
            val["fecha_entrega"]= val.get("fecha_esperada")

        if val.get("estado") == "Entregado":

            if val.get("fecha_esperada")[5:7] == "01" or val.get("fecha_entrega")[5:7] == "01" :
                AllPedEntEnero.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "estado": val.get("estado"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return AllPedEntEnero


#start = datetime.strptime(date_1, "%Y/%m/%d")
# end = datetime.strptime(date_, "%Y/%m/%d")

