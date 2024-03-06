import storage.pago as pag

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
    codigosclientespago2008 = [{k: v for k, v in item} for item in codigosclientespago2008]

    return codigosclientespago2008
