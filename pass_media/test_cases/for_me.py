import requests, json
from datetime import datetime, timedelta
import data_tests as dt
import variables as var
from functions.cookies import Sessions
from functions.emails import Emails
from functions.accounts import Accounts


env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)



data1 = {"birthdate":"11.01.1910"}
data2 = {"birthdate":"11.01.2000"}

a = Accounts().update_account_info(data2)
print(a.text)
b = Accounts().get_account_info()
print(b.json()['birthdate'])
#assert req == r
'''
#.strftime("%d.%m.%Y")
now = datetime.now().date() 
data_need = now.year+2
print(data_need)
'''