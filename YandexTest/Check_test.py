from init import *

#Записываем в разные строчки все Json'ы для post/put
#Для тестов можно менять содержимое файлов
if True:
    jspo = ""
    with open("postPetOK.json", "r") as f:
        for line in f:
            jspo += line
    jspf = ""
    with open("postPetF.json", "r") as f:
        for line in f:
            jspf += line
    jsso = ""
    with open("postStoreOK.json", "r") as f:
        for line in f:
            jsso += line
    jssf = ""
    with open("postStoreF.json", "r") as f:
        for line in f:
            jssf += line
    jsuo = ""
    with open("postUserOK.json", "r") as f:
        for line in f:
            jsuo += line
    jsuo2 = ""
    with open("postUserOK2.json", "r") as f:
        for line in f:
            jsuo2 += line
    jsuo3 = ""
    with open("postUserOK3.json", "r") as f:
        for line in f:
            jsuo3 += line
    jsuf = ""
    with open("postUserF.json", "r") as f:
        for line in f:
            jsuf += line


#____GET____
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


#___DELETE___
def test_DP1(): #OK
    a = DELETE_Pet(1).status_code
    assert a == 200
def test_DP2(): #Not Found
    a = DELETE_Pet(167287648624717821).status_code
    assert a == 404

def test_DO1(): #OK
    a = DELETE_Ord(1).status_code
    assert a == 200
def test_DO1(): #Not Found
    a = DELETE_Ord(1564875687546).status_code
    assert a == 404

def test_DU1(): #OK
    a = DELETE_User('aaa').status_code
    assert a == 200
def test_DU1(): #Not Found
    a = DELETE_User('1564875ghfvyfbi687546').status_code
    assert a == 404


#___PUT___

def test_PP1(): #OK
    a = PUT_Pet(jspo).status_code
    assert a == 200
def test_PP2(): #ERROR
    a = PUT_Pet(jspf).status_code
    assert a == 400

def test_PU1(): #OK
    a = PUT_User('aaa', jsuo)
    if a:
        assert a.status_code == 200
    else:
        assert False
def test_PU2(): #ERROR
    a = PUT_User('aaa', jsuf)
    if a:
        assert a.status_code == 400
    else:
        assert False
def test_PU_name(): #Check does new user exist
    a = PUT_User('aaa', jsuo)
    new_user = json.loads(jsuo)
    name = new_user["username"]
    a = GET_User_Name(name).status_code
    assert a == 200

#___POST___
def test_POP1(): #OK
    a = POST_Pet(jstrPet=jspo).status_code
    assert a == 200
def test_POP2(): #ERROR
    a = POST_Pet(jstrPet=jspf).status_code
    assert a == 400
def test_POP_existing(): #Does this user exist
    POST_Pet(jstrPet=jspo)
    new_pet = json.loads(jspo)
    a = GET_Pet(new_pet["id"]).status_code
    assert a == 200

def test_POPU1(): #OK
    a = POST_Pet_Update(1, 'name', 'status').status_code
    assert a == 200
def test_POPU1(): #ERROR Not found 404
    a = POST_Pet_Update(1982575872359875230, 'name', 'status').status_code
    assert a == 404
def test_POPU_ns(): #Check new name + status
    id = 1
    name = 'aaa'
    status = 'newstatus'
    POST_Pet_Update(id, name, status)
    new_pet_j = json.loads(GET_Pet(id).text)
    assert new_pet_j["name"] == name and new_pet_j["status"] == status

def test_POSO1(): #OK
    assert POST_Store_Ord(jsso).status_code == 200
def test_POSO2(): #Error
    assert POST_Store_Ord(jssf).status_code == 400
def test_POSO_work(): #Check if works
    POST_Store_Ord(jsso)
    id = json.loads(jsso)["id"]
    assert GET_Store_OrdId(id).status_code == 200

def test_POU1(): #OK
    assert POST_User(jsuo).status_code == 200
def test_POU2(): #ERROR
    assert POST_User(jsuf).status_code == 400
def test_POU_work(): #Check if works
    POST_User(jsuo)
    name = json.loads(jsuo)["username"]
    assert GET_User_Name(name).status_code == 200

def test_POUL1(): #OK
    a = POST_User_List([jsuo, jsuo])
    arr = []
    for i in a:
        arr.append(i.status_code != 200)
    assert not any(arr)
def test_POUL2(): #ERROR
    a = POST_User_List([jsuo, jsuf])
    arr = []
    for i in a:
        arr.append(i.status_code != 200)
    assert any(arr)
def test_POUL_work(): #Check if works
    li = [jsuo, jsuo2, jsuo3]
    POST_User_List(li)
    arr_names = []
    arr_check = []
    for i in li:
        arr_check.append(json.loads(i)["username"])
    for name in arr_names:
        arr_check.append(GET_User_Name(name).status_code != 200)
    assert not any(arr_check)