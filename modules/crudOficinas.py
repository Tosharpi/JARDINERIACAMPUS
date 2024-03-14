import json
import requests

def getAllDataOfice():
    peticion = requests.get("http://172.16.103.33:5005")
    data = peticion.json()
    return data