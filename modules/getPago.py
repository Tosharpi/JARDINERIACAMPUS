import storage.pago as pag

def getCodClientesPago2008():
    getCodClientesPago2008 = []
    for val in pag.pago:
        año=val.get("fecha_pago")

        if año[0:4]== "2008":
            getCodClientesPago2008.append(
                {
                    "fecha_pago" : {val.get("fecha_pago")},
                    "codigo_cliente" : {val.get("codigo_cliente")}
                }
            )
            getCodClientesPago2008=set(getCodClientesPago2008)
            getCodClientesPago2008=list(getCodClientesPago2008)

    return getCodClientesPago2008