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
