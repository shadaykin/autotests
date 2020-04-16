import requests, json, time
import variables as var
from selenium import webdriver
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts


env = var.stand_for_test
acc = Accounts()
service = var.options['cas']

response = acc.get_account_info(service).json()
need_update = []
requireds = response['required_fields']

for required in requireds:
    have = response[required]
    if have == '' or have == []:
        print(required)
        need_update.append(required)
data = acc.generate_account_data(need_update)
if data == {}:
    pass
else:

#upd = acc.update_account_info(data)

