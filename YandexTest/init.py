import requests
import json
json_string = ""
with open("post.json", "r") as f:
    for line in f:
        json_string += line
urldef = 'https://petstore.swagger.io/v2/'
# new_pet = json.loads(json_string)
# idpet = new_pet["id"]
idpet = 1


def GET_Pet(id: int):
    url = urldef + f'pet/{id}'
    return requests.get(url)

def GET_Pet_Status(stat: str):
    url = urldef + f"pet/findByStatus?status='{stat}'"
    return requests.get(url)

def GET_Store_Inv():
    return requests.get(urldef+'store/inventory')

def GET_Store_OrdId(id: int):
    url = urldef+ f'store/order/{id}'
    return requests.get(url)

def GET_User_Name(name: str):
    url = urldef + f'user/{name}'
    return requests.get(url)

def GET_User_LI(name:str, passw:str):
    url = urldef + f"user/login?username='{name}',password='{passw}'"
    return requests.get(url)

def GET_User_LO():
    return requests.get(urldef+'user/logout')

def DELETE_Pet(id:int):
    url = urldef + f'pet/{id}'
    return requests.delete(url)

def DELETE_Ord(id:int):
    url = urldef + f'store/order/{id}'
    return requests.delete(url)

def DELETE_User(name: str):
    url = urldef + f'user/{name}'
    return requests.delete(url)


# post = requests.post(f'{urldef}pet', json=json_string, headers={"Content-Type": "application/json"})
aaa = DELETE_Pet(21)