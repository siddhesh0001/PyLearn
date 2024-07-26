#Marking the test cases using pytest
#We can divide pur test cases using mark
#We have to use annotations to mark the test cases
#ie pytest -m smoke

import pytest
@pytest.mark.smoke #--> We will mark our test cases using this annotation
def test_sub0():
    assert 2-2 == 0

@pytest.mark.regration
def test_sub1():
    assert 3-3 == 0

@pytest.mark.smoke
def test_sub2():
    assert 1-1 == 0

@pytest.mark.sanity
def test_sub3():
    assert 0-0 != 0

@pytest.mark.skip(reason =  "I don't want to run this test case")
def test_sub4():
    assert 0 - 0 != 0

#now we will use pytest -m smoke and file name to run all smoke mark test cases