import requests
import json
import threading


def yoz(lnk: str):
    with open("file.txt", "w") as reader:
        response = requests.get(url=lnk)
        reader.write(response.text)


threader0 = threading.Thread(target=yoz("https://jsonplaceholder.typicode.com/posts"))


def jsono(lnk: str):
    with open("file.json", "w") as reader:
        response = requests.get(url=lnk)
        json.dump(response.json(), reader)


threader1 = threading.Thread(target=jsono("https://jsonplaceholder.typicode.com/albums"))


def jsonr(file_n: str):
    with open(file_n, 'r') as reader:
        print(reader.read())


threader2 = threading.Thread(target=jsonr("file.json"))

threader0.start()
threader1.start()
threader2.start()
