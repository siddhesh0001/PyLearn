#there are few rule to use pytest and how to install pytest
# 1 pip install pytest
# 2 File name  --> it should be test_name_of_file
# 3 Test name - it should be test.nameoftest() :
# 4 Assert - It means Actual result = expected result

def test_addation():
    assert 2+2 == 4
    assert 2+3 == 5

def test_substraction():
    assert 5-3 == 2
    assert 10-20 == -10