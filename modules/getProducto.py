import storage.producto as prod
from tabulate import tabulate

def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in prod.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("price_venta")
    condiciones.sort(key=price)

    return condiciones

def menu():

    while True:
            
        print("""
            MENU  PRODUCTOS
            
            1. Obtener todos los productos segun su gama y su stock (gama, stock)
        """)
        opcion = int(input("Seleccione una de las opciones: "))
        if opcion == 1:
            gama = input("Ingrese la gama: ")
            stock = int(input('ingrese el stock: '))
            print(tabulate(getAllStockPriceGama(gama, stock)))
