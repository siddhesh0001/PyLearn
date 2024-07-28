#Now we will do CURD opperation


import pytest
import allure
import requests

@allure.title("Create booking CRUD")
@allure.description("TC1 - verify create booking")
@pytest.mark.CRUD
def test_create_booking_with_positive():
    #While sending request we need to make request
    # ie url, method(post), header,payload, Auth
    base_url = "https://restful-booker.herokuapp.com"  #this is base url ie main url
    base_path = "/booking" #this is path
    URL = base_url + base_path #this is full url
    headers = {"Content-type" : "application/json"}
    #now we will add payload --> This is data which we are sending to server to create booking
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

        #Now we will send post request
    response = requests.post(url=URL, headers=headers, json=payload)
    #responseData = response.json()
    #or we can use mention below
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
    # or we can write in different way
    # firstname = response.json()["bookingid"]["firstname"]
    # assert firstname == "sid"



@allure.title("Create booking CRUD")
@allure.description("TC2 - verify create booking")
@pytest.mark.CRUD
def test_create_booking_with_negative_1():
    base_url = "https://restful-booker.herokuapp.com"  # this is base url ie main url
    base_path = "/booking"  # this is path
    URL = base_url + base_path  # this is full url
    headers = {"Content-type": "application/json"}
    payload = {

    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 500


@allure.title("Create booking CRUD")
@allure.description("TC3 - verify create booking")
@pytest.mark.CRUD
def test_create_booking_with_negative_2():
    base_url = "https://restful-booker.herokuapp.com"  # this is base url ie main url
    base_path = "/booking"  # this is path
    URL = base_url + base_path  # this is full url
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "sid",
        "lastname": "Kasar",
        "totalprice": 111,
        "depositpaid": -1,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    response = requests.post(url=URL, headers=headers, json=payload)
    responseData = response.json()
    print(URL)
    print("This is payload",payload)
    print("This is response",responseData)
    assert response.json()["booking"]["depositpaid"] == True
