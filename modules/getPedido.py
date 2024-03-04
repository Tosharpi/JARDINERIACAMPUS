import storage.pedido as ped 

def getCodigoPedido(codigoPed):
    for val in ped.pedido:
        if (val.get('codigo_pedido') == codigoPed):
            return {
            "codigo_pedido":{val.get('codigo_pedido')},
            "codigo_cliente":{val.get('codigo_cliente')}
           }
