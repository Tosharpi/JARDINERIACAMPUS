import json
import requests

def getAllDataPedidos():
    
    peticion = requests.get("http://172.16.103.33:5007")
    data = peticion.json()
    return data