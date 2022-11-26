from fruit import *
from cryptoc import *
import requests
import json


def request(url):
    try:
        answer = requests.get(url)
        if answer.status_code == 200:
            return answer.text
    except Exception as error:
        print(error)


def parsing(answer):
    try:
        return json.loads(answer)
    except Exception as error:
        print(error)


def menu():
    while True:
        print("=-=          -           =-=")
        print("1 - [Fruit] API ")
        print("2 - [Crypto]currency API")
        print("0 - [Exit]")
        print("=-=          -           =-=")
        option = input(": ").lower()
        match option:
            case "fruit" | "1":
                baseText = request(URL_FRUIT)   # request the json of everything on the API
                clearText = parsing(baseText)   # store and transforms all information into a list
                fruitmenu(clearText)
            case "crypto" | "2":
                baseText = request(URL_CRYPTO)  # request the json of everything on the API
                clearText = parsing(baseText)   # store and transforms all information into a list
                cryptomenu(clearText)
            case "exit" | "0":
                break


if __name__ == "__main__":
    menu()
