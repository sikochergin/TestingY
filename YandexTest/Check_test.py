from init import *
idp = 111
ido = 1
name = 'ko4gin'
ps = 'available'
def test_GP1(): #existing pet
    a = GET_Pet(1).status_code
    assert a == 200
def test_GP2(): #non-existing pet
    a = GET_Pet(123213).status_code
    assert a == 404
def test_GP3(): #ID text
    a = GET_Pet('Yandex').status_code
    assert a == 404 

def test_GPS1(): #OK
    a = GET_Pet_Status('available').status_code
    assert a == 200

def test_GSI1(): #OK always
    a = GET_Store_Inv().status_code
    assert a == 200

def test_GSO1(): #OK
    a = GET_Store_OrdId(1).status_code
    assert a == 200
def test_GSO2(): #non-existing order
    a = GET_Store_OrdId(123434233).status_code
    assert a == 404
def test_GSO3(): #--||--
    a = GET_Store_OrdId('Yandex').status_code
    assert a == 404

def test_GUN1(): #OK
    a = GET_User_Name('aaa').status_code
    assert a == 200
def test_GUN2(): #non-existing name
    a = GET_User_Name('yandexxxxxxxxxxxx').status_code
    assert a == 404
def test_GUN3(): #--||--
    a = GET_User_Name(1).status_code
    assert a == 404

def test_GULI(): #OK
    a = GET_User_LI('aaa', '111').status_code
    assert a == 200

def test_GULO1(): #OK always
    a = GET_User_LO().status_code
    assert a == 200