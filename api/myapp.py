import requests
import json

URL = "http://127.0.0.1:8000/studentapi"

def get_data(id=None):
    data = {
       
    }
    header={'content-type: application/json'}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data , headers=header)
    data =r.json()
   
    print(data)

# get_data()

def post_data():
    data = {
  'name': 'Muhammad Zain',
  'roll':150,
  'city':'Kasur'
    }
    header={'content-type: application/json'}
    json_data = json.dumps(data)
    r=requests.post(url=URL, data=json_data,headers=header)
    data=r.json()
    print(data)


post_data()
def put_data():
    data = {
    'id':4,
  'name': 'Muhammad Tayyab',
  'roll':600,
  'city':'islamabad'
  
  
    }
    header={'content-type: application/json'}
    json_data = json.dumps(data)
    r=requests.put(url=URL, data=json_data,headers=header)
    data=r.json()
    print(data)
# put_data()



def delete_data():
    data = {'id':12}
    header={'content-type: application/json'}
    json_data = json.dumps(data)
    r=requests.delete(url=URL, data=json_data,headers=header)
    data=r.json()
    print(data)
# delete_data()