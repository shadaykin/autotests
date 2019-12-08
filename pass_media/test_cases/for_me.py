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


service='https://matchtv.ru'

ff1 = Accounts().get_account_info(service)
req = ff1.json()['required_fields']
r = req
print(r)
#assert req == r
'''
#.strftime("%d.%m.%Y")
now = datetime.now().date() 
data_need = now.year+2
print(data_need)
'''