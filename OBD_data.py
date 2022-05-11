
import requests
import time


def rpm():
    pass



def temperature():
    pass


def send_data(url=None, json_data=None):

    requests.post(url, json_data)




def main():
    url = "http://127.0.0.1:8000/OBD_get_data"

    # json_data={
    #     "rpm": 5500,
    #     "temp": 60

    # }
    for _ in range(10):
        send_data(url)
        time.sleep(1)

if __name__ == '__main__':
    main()
