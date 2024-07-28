#now we will do put request
#What we need for PUT request
# URL,Path, booking id (valid), token(auth), payload
#so before put request we need to create auth token and booking id
#so we need to create booking first

import pytest
import allure
import requests

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


def create_booking():

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type" : "application/json"}
    payload ={
        "firstname": "sid",
        "lastname": "Kasar",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


    response = requests.post(url=URL, headers=headers, json=payload)
    bookingid  = response.json()["bookingid"]
    return bookingid
    print(response)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["bookingid"] > 0

    assert response.json()["booking"]["firstname"] == "sid"
    assert response.json()["booking"]["lastname"] == "Kasar"
    assert response.json()["booking"]["totalprice"] == 111
    assert response.json()["booking"]["depositpaid"] == True
    assert response.json()["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response.json()["booking"]["bookingdates"]["checkout"] == "2019-01-01"

def test_put_request_postive():
    base_url ="https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {"Content-type": "application/json", "Cookie": cookie}

    json_payload = {
        "firstname": "Siddhesh",
        "lastname": "Kasar",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    respone =requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert respone.status_code == 200
    assert respone.json()["firstname"] == "Siddhesh"
    print(respone.json())

def test_delete_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {"Content-type": "application/json", "Cookie": cookie}
    response = requests.delete(url=PUT_URL, headers=headers)
    assert response.status_code == 201







