import json
import requests

def getAllGama():
    peticion = requests.get("http://172.16.103.32:5002", timeout=10)
    data = peticion.json
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
