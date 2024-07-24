import requests
import json
json_string = ""
with open("postPetOK.json", "r") as f:
    for line in f:
        json_string += line
urldef = 'https://petstore.swagger.io/v2/'



def GET_Pet(id):
    url = urldef + f'pet/{id}'
    return requests.get(url)

def GET_Pet_Status(stat):
    url = urldef + f"pet/findByStatus?status='{stat}'"
    return requests.get(url)

def GET_Store_Inv():
    return requests.get(urldef+'store/inventory')

def GET_Store_OrdId(id):
    url = urldef+ f'store/order/{id}'
    return requests.get(url)

def GET_User_Name(name):
    url = urldef + f'user/{name}'
    return requests.get(url)

def GET_User_LI(name, passw):
    url = urldef + f"user/login?username='{name}',password='{passw}'"
    return requests.get(url)

def GET_User_LO():
    return requests.get(urldef+'user/logout')



def DELETE_Pet(id):
    url = urldef + f'pet/{id}'
    return requests.delete(url)

def DELETE_Ord(id):
    url = urldef + f'store/order/{id}'
    return requests.delete(url)

def DELETE_User(name):
    url = urldef + f'user/{name}'
    return requests.delete(url)


def POST_Pet(jstrPet):
    return requests.post(f'{urldef}pet', json=jstrPet)

def POST_Pet_Update(id, name, status):
    pet = GET_Pet(id).text
    new_pet = json.loads(pet)
    new_pet["name"] = name
    new_pet["status"] = status
    return POST_Pet(new_pet)

def POST_Store_Ord(jsonStore):
    return requests.post(f'{urldef}store/order', json = jsonStore)

def POST_User_List(arr):
    li = []
    for js in arr:
        li.append(requests.post(f'{urldef}user', json=js))
    return li

def POST_User(js):
    return requests.post(f'{urldef}user', json=js)



def PUT_Pet(js):
    return POST_Pet(js)

def PUT_User(name, js):
    us = GET_User_Name(name)
    if us.status_code == 200:
        DELETE_User(name)
        return POST_User(js)
    else:
        return None