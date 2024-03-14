import json
import requests

def getAllDataPago():
    peticion = requests.get("http://172.16.103.33:5006")
    data = peticion.json()
    return data