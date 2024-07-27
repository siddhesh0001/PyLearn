#Request module
#it is a package or library which is used to make HTTP requests
#it is package or library contain function which we can use easily
#ie math, os, csv,pie etc
#It means we are borrowing functions from other people

# Now if ew want to do for GET request what is needed
# Request we need ( Client to server)
# ie GET request - Booking id
# URL -  needed
# Auth - no need now
# Payload - no need
# Headers - no need
# Content-type - no need
# Query parameters - no need
# Path parameters - Needed

# Response
# What we will get
# Body --> We will verify using asserts
#      --> We will verify Key and values
# Status code
# Time
# Json schema, xml schema

# To import request module --> Install it first using pip install requests

import pytest
import allure
import requests

@allure.title("Test GET request for RestBooker Project")
@allure.description("Verify the response of GET request with Correct ID")
@allure.tag("Regression", "Smoke")
@allure.label("owner", "Siddhesh")
@allure.testcase("TC-001")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response = requests.get(url)
    print(response.json())
    print(response.headers)
    print(response.cookies)
    assert response.status_code == 200


@allure.title("Test GET request for RestBooker Project")
@allure.description("Verify the response of GET request with Invalid ID")
@allure.testcase("TC-002")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
   # print(responseData.json())
    assert responseData.status_code == 404

@allure.title("Test GET request for RestBooker Project")
@allure.description("Verify the response of GET request with Invalid ID")
@allure.testcase("TC-003")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
   # print(responseData.json())
    assert responseData.status_code == 200


