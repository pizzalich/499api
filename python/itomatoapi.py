# Python Api for I-Tomato
# Marc Bonwick
# 24 June 2019

# importing the requests library
import requests
from requests.exceptions import HTTPError
import json

# api-endpoint
DATAURL = "https://itomato-server.herokuapp.com/crud"
IMAGEURL = "https://itomato-server.herokuapp.com/crud/image"


def itomatoGetData():
    try:
        response = requests.get(DATAURL)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        response = requests.get(url=DATAURL)
        data = response.json()
        print(data)
        return data


def itomatoPostData(
        temp=999,
        humidity=-1,
        light=-1,
        moisture=-1):
    body = {'temp': temp, 'humidity': humidity,
            'light': light, 'moisture': moisture}
    print(body)
    response = requests.post(DATAURL, json=body)
    print(response.json)
    if response.status_code == 200:
        print("POST OK")
    else:
        print("POST ERROR:", response.status_code, response.reason)


def itomatoGetImage():
    # TODO:FIX THIS

    try:
        response = requests.get(IMAGEURL)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        response = requests.get(url=IMAGEURL)
        data = response.json()
        return data


def itomatoPostImage(image={}):
    # TODO: FIX THIS
    body = {'image': image}
    response = requests.post(IMAGEURL, json=body)
    print(response.json)
    if response.status_code == 200:
        print("POST OK")
    else:
        print("POST ERROR:", response.status_code, response.reason)
