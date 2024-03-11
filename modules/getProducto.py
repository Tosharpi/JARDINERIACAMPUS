import storage.producto as prod
from tabulate import tabulate

def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in prod.producto:
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price)

    return condiciones

def getStockProduct(codProd):
    StockProduct = []
    for val in prod.producto:
        if val.get("codigo_producto") == codProd:
            StockProduct.append({
            "codProd":val.get("codigo_producto"),
            "nombre":val.get("nombre"),
            "stock":val.get("cantidad_en_stock")
        })
        
    return StockProduct
def menu():

    while True:
            
        print("""
            MENU  PRODUCTOS
            
            1. Obtener todos los productos segun su gama y su stock (gama, stock)
            2. Obtener el stock de un producto segun su codigo (codigo producto)
        """)
        opcion = int(input("Seleccione una de las opciones: "))
        if opcion == 1:
            gama = input("Ingrese la gama: ")
            stock = int(input('ingrese el stock: '))
            print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))
        if opcion == 2:
            codProd = input('Ingrese el codigo del producto: ')
            print(tabulate(getStockProduct(codProd), headers="keys", tablefmt="github"))
