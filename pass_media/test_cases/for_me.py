import requests, json, time
import variables as var
from frontend.authorization.phone import Test
#from functions.cookies import Sessions
from selenium import webdriver
#from functions.emails import Emails
#from functions.accounts import Accounts
#from functions.services import Services




obj = Test().get()

print(obj)
'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

req = session.get('https://passport.test-201.zxz.su/api/cities/autocomplete/')
print(req.text)
'''



#print(data["results"][1]["full_name"])