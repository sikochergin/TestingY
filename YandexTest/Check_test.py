from init import *
idp = 111
ido = 1
name = 'ko4gin'
ps = 'available'
def test_GP():
    a = GET_Pet(idp).status_code
    assert a == 200
def test_GPS():
    a = GET_Pet_Status(ps).status_code
    assert a == 200
def test_GSI():
    a = GET_Store_Inv().status_code
    assert a == 200
def test_GSO():
    a = GET_Store_OrdId(ido).status_code
    assert a == 200
def test_GUN():
    a = GET_User_Name(name).status_code
    assert a == 200