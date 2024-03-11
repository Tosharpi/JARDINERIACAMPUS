import storage.pago as pag
from datetime import datetime

def getCodClientesPago2008():
    codigosclientespago2008 = []
    for val in pag.pago:
        año = val.get("fecha_pago")

        if año.startswith("2008"):  
            codigosclientespago2008.append(
                {
                    "fecha_pago": val.get("fecha_pago"),
                    "codigo_cliente": val.get("codigo_cliente")
                }
            )

    codigosclientespago2008 = list(set(tuple(item.items()) for item in codigosclientespago2008))

    return codigosclientespago2008


def getAllPagPayPal():
    AllPagPayPal = []
    for val in pag.pago:

        pago= "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(pago, "%d/%m/%Y")

        if(val.get("forma_pago") == "PayPal" and start.year == 2008):
            AllPagPayPal.append({
                "forma_pago" :(val.get("forma_pago")),
                "fecha_pago" :(val.get("fecha_pago")),
                "total": (val.get("total"))
            })

    AllPagPayPal = sorted(AllPagPayPal, key=lambda x: x["total"], reverse=True)

    return AllPagPayPal

def getAllFormasPago():
    FormasPago = list()
    for FP in pag.pago:
        if(FP.get("forma_pago") != None):
            FormasPago.append({
                "forma_pago" : (FP.get("forma_pago"))
            })

    FormasPago = list(set(tuple(item.items()) for item in FormasPago))
    
    return FormasPago

def menu():
    print("""
    MENU DE PAGO
          
          1. Obtener todos los clientes que realizaron un pago en el 2008
""")