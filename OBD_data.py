
from ast import Try
from mimetypes import init
from socket import timeout
import requests
import time
import json





class Car:
    """ Initial the basic car class """
    def __init__(self, username: str, brand: str, engine_CC: int, engine_code: str):
        
        self.username = username
        self.brand = brand
        self.engine_CC = engine_CC
        self.engine_code = engine_code

        temperature = 0
        rpm = 0

        # // self 
        def __str__(self):
            return f"Username: {self.username}, Brand: {self.brand}, Engine CC: {self.engine_CC}, Engine code: {self.engine_code}"

    def rpm():
        pass


    def temperature():
        pass
    

"""DATA CAME FROM THE REAL ENGINE THROE OBD"""
def collect_data():
    pass




def send_data(url, data):

    try:

        server_response = requests.post(url, json=data, timeout=30)
        print(f"Server sended status code: {server_response.status_code}")

    except:
        print(f"Server sended status code: {server_response.status_code}")



def main() -> None:
    url = "http://127.0.0.1:8000/OBD_get_data"

    datas = {
        "rpm": 5500,
        "temp": 60}


    MyOpel = Car("ZsoltD", "Opel Astra", 1.4, "14BZY")
    print(MyOpel)




    while(True):

        # send_data(url, json.dumps(json_data), timeout=30, verify=False)
        send_data(url, datas)

        time.sleep(1)


if __name__ == '__main__':
    main()
