
import json
import requests

def postProducto(producto):
    #json-server storage/productos.json -b 5001
    peticion = requests.post("http://172.16.100.136:5002", data=json.dumps(producto))
    res = peticion.json()
    return res