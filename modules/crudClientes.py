import json
import requests

def getAllDataClient():

    peticion = requests.get("http://172.16.103.33:5003")
    data = peticion.json()
    return data