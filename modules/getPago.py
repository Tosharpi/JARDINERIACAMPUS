import os
from datetime import datetime
from tabulate import tabulate
import modules.crudClientes as crudCli
import modules.crudPago as crudPag
import modules.crudEmpleados as crudEmpl

#:)

def getCodClientesPago2008():
    codigosclientespago2008 = []
    for val in crudPag.getAllDataPago():
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
    for val in crudPag.getAllDataPago():

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
    for FP in crudPag.getAllDataPago():
        if(FP.get("forma_pago") != None):
            FormasPago.append({
                "forma_pago" : (FP.get("forma_pago"))
            })

    FormasPago = list(set(tuple(item.items()) for item in FormasPago))
    
    return FormasPago

def getAllClientPag():
    allClientPag =[]
    for val in crudPag.getAllDataPago():
        for val2 in crudCli.getAllDataClient():
            for val3 in crudEmpl.getAllDataEmpl():
                if val2.get("codigo_cliente") == val.get("codigo_cliente") and val2.get("codigo_empleado_rep_ventas") == val3.get("codigo_empleado"): 

                    allClientPag.append(
                        {
                            "codigo_cliente":val.get("codigo_cliente"),
                            "nombre":val2.get("nombre_cliente"),
                            "cod_representante": val2.get("codigo_empleado_rep_ventas"),
                            "nombre_empleado": val3.get("nombre")
                        }
                    )
    return allClientPag

def getAllNoPay():
    allNoPay = []
    for val in crudCli.getAllDataClient():
        pagos = False
        for d in crudPag.getAllDataPago():
                if val.get('codigo_cliente')== d.get('codigo_cliente'):
                    pagos = True
                    break
        if not pagos:
            for d in crudEmpl.getAllDataEmpl():
                if val.get('codigo_empleado_rep_ventas') == d.get('codigo_empleado'):
                    if d.get('puesto') == 'Representante Ventas':
                        allNoPay.append({

                                'codigo': val.get('codigo_cliente'),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "puesto": d.get("puesto"),
                                "Representante de ventas": d.get('nombre')
                            })
    return allNoPay

def menuReportesPago():
    while True:
        os.system("clear")
        print("""
        MENU DE PAGO
            
            0. Salir
            1. Obtener todos los clientes que realizaron un pago en el 2008
            2. Obtener todos los clientes que pagaron con PayPal
            3. Obtener todas las formas de pago
            4. Obtener todos los clientes que realizaron un pago, junto con sus representantes
            5. Obtener todos los clientes que no realizaron un pago, junto con sus representantes
            
    """)
        
        opcion = int(input('Seleccione la opcion: '))
        if (opcion == 1):
            print(tabulate(getCodClientesPago2008(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 2):
            print(tabulate(getAllPagPayPal(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 3):
            print(tabulate(getAllFormasPago(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 4):
            print(tabulate(getAllClientPag(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 5):
            print(tabulate(getAllNoPay(), headers="keys", tablefmt="github"))
            input('Para continuar oprima alguna tecla...')
        elif (opcion == 0):
            break
    