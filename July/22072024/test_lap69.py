#Now we will create a proper report for this using allure report
#we have to install it first using pip install allure-pytest

import pytest
import allure   #--> This is the package we have to install

@allure.title("TC1 To verify the sub function")
@allure.description("We can give test description here") #we have allure. othere action too
@pytest.mark.smoke #--> We will mark our test cases using this annotation
def test_sub0():
    assert 2-2 == 0

@allure.title("TC2 To verify the sub function")
@allure.description("We can give test description here")
@pytest.mark.regration
def test_sub1():
    assert 3-3 == 0

@allure.title("TC3 To verify the sub function")
@allure.description("We can give test description here")
@pytest.mark.smoke
def test_sub2():
    assert 1-1 == 0


@allure.title("TC4 To verify the sub function")
@allure.description("We can give test description here")
@pytest.mark.sanity
def test_sub3():
    assert 0-0 == 0


@allure.title("TC To verify the sub function")
@allure.description("We can give test description here")
@pytest.mark.skip(reason =  "I don't want to run this test case")
def test_sub4():
    assert 0 - 0 != 0

