import json
import requests

def getAllGama():
    #json-server storage/gama_producto.json -b 5003
    peticion = requests.get("http://172.16.100.136:5003")
    data = peticion.json
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
