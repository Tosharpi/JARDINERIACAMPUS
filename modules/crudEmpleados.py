import json 
import requests

def getAllDataEmpl():
    
    peticion = requests.get("http://172.16.103.33:5004")
    data = peticion.json()
    return data

