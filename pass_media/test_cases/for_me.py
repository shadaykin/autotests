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

msc = 'q=Моск'
req_msc = session.get(var.options[env]+var.endpoints_account['city'],params = msc)
print(req_msc.text)
'''
#.strftime("%d.%m.%Y")
now = datetime.now().date() 
data_need = now.year+2
print(data_need)
'''