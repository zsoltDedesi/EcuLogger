
from socket import timeout
import requests
import time
import json

def rpm():
    pass


def temperature():
    pass


def send_data(url, data):


    # files = {'json': (None, json.dumps(data), 'application/json')}


    server_response = requests.post(url, json=data, timeout=30)

    print(f"Server sended status code: {server_response.status_code}")
    print(f"Json status: {server_response.json()}")


def main():
    url = "http://127.0.0.1:8000/OBD_get_data"

    datas = {
        "rpm": 5500,
        "temp": 60}






    for _ in range(10):

        # send_data(url, json.dumps(json_data), timeout=30, verify=False)
        send_data(url, datas)

        time.sleep(1)


if __name__ == '__main__':
    main()
