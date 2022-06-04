
from logging import exception
from mimetypes import init
from socket import timeout
from tkinter import E
from unicodedata import name
from venv import create
import requests
import time
import json





class Car:
    """ Initial the basic car class """
    def __init__(self, username: str, brand: str, engine_CC: int, fuel: str, engine_code: str):
        
        self.username = username
        self.brand = brand
        self.engine_CC = engine_CC
        self.engine_code = engine_code
        self.fuel = fuel

    def __str__(self) -> str:
        return f"Username: {self.username} Brand: {self.brand}, Engine CC: {self.engine_CC}, Type of fuel: {self.fuel}, Engine code: {self.engine_code}"
        
        """Init message"""
    def to_string(self) -> str:
        print("================================== INITIALIZATION ==================================")
        print("The Car has been initialized with the following informations")
        print(f"Username: {self.username} Brand: {self.brand}, Engine CC: {self.engine_CC}, Type of fuel: {self.fuel}, Engine code: {self.engine_code}")
        print("\n")

    def rpm(self) -> int:
        pass


    def temperature(self) -> int:
        pass
    


"""TODO NEED TO DELETE AFTER IMPLEMENTING collect_data METHOD"""
def create_test_data(number_of_set=None) -> dict:
    
    print("================================== Create dummy data ==================================")
    temperature = []
    rpm = []
    
    if number_of_set is None:
        print("There is no number set")
        return
        
        
    for element in range(number_of_set):
        
        temperature.append(element)
        rpm.append(element * 2 + 800)
    
    # print("Data ha been created with the following: \n")
    # print("Temperature: ",*temperature, "\n")
    # print("RPM: ",*rpm, "\n")
    print("================================== Createation finished ==================================\n")
    
    return {"temp": temperature, 
            "rpm": rpm}

    
    
class DataManaging:
    
    def __init__(self, url_path) -> None:

        self.url_path = url_path
        self.data = create_test_data(100)
        self.time_out = 30
        self.stop_sending = 5

    """DATA CAME FROM THE REAL ENGINE THROE OBD"""
    def collect_data():
        pass


    def send_data(self) -> None:

        try:
            server_response = requests.post(self.url_path, json=self.data, timeout=self.time_out)
            print(f"The data has benn sent, status code: {server_response.status_code}")

        except requests.ConnectionError as connError:
            print(f"Connection error!, Please check the internet connection")
            print(f"Connection error message: {connError} \n")

            self.stop_sending -= 1 
            print(f"Reconnection try left: {self.stop_sending}")

            if (self.stop_sending == 0):
                print("The number of reconnection reached 5 times. \nEnd of reconnection process")
                return

            # Setting the sleep time between 2 sending (sec)
            # time.sleep(300)
            time.sleep(1)
            self.send_data()

        except Exception as e:
            print("Something Wrong!")
            print(f"error message: {e.error}")


    def __str__(self) -> str:
        return f"This is a collected dummy data: {self.data}"



def main() -> None:

    
    MyOpel = Car(username="ZsoltD", brand="Opel Astra", engine_CC=1.4, fuel="gasoline", engine_code="14BZY")
    MyOpel.to_string()


    """SETTING THE REQUIRED URL"""
    url = "http://127.0.0.1:8000/OBD_get_data"
    data_man = DataManaging(url_path=url)
    # print(data_man)

    count = 10

    while(True):

        data_man.send_data()
        print(f" {count}")

        time.sleep(2)
        count -= 1

        if count == 0:
            break


if __name__ == '__main__':
    main()
