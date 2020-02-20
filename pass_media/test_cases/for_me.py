import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import response_service as resp_acc
import variables as var
#from functions.cookies import Sessions
from selenium import webdriver
#from functions.emails import Emails
#from functions.accounts import Accounts
#from functions.services import Services

'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

req = session.get('https://passport.test-201.zxz.su/api/cities/autocomplete/')
print(req.text)
'''
data = {
  "count": 169653,
  "next": "http://passport.test-201.zxz.su/api/cities/autocomplete/?page=2",
  "previous": None,
  "results": [
    {
      "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
      "title": "Москва",
      "region": None,
      "area": None
    }
  ]
}


print(data['count'])
assert data['results'][0]['title'] == 'Москва'
assert data['results'][0]['region'] == None
assert data['results'][0]['area'] == None
assert len(data['results'][0]['city_guid']) != 0



#print(data["results"][1]["full_name"])