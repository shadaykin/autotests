import requests, json, time
import variables as var
#from frontend.functions.phone import Test
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

browser = webdriver.Chrome()

print(cookie)