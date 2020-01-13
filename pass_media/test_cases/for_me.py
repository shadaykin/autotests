import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import response_service as resp_acc
import variables as var
#from functions.cookies import Sessions
from selenium import webdriver
from functions.emails import Emails
from functions.accounts import Accounts
from functions.services import Services

'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)
'''

pmid = Services().get_pmid()
field_90 = ['first_name', 'last_name', 'nickname', 'city', 'gender', 'birthdate', 'email']
field_50 = ['first_name', 'last_name', 'email']

data_90 = Accounts().generate_account_data(field_90)
data_50 = Accounts().generate_account_data(field_50)

clear = Accounts().update_all_account_info('empty')
delete = Emails().emails_delete_unconfirmed()
delete = Emails().emails_delete_confirmed()

upd_data_50 = Accounts().update_account_info(data_50)
fullness_50 = Accounts().get_profile_fullness(pmid)
print(fullness_50.text)

clear = Accounts().update_all_account_info('empty')
delete = Emails().emails_delete_unconfirmed()
delete = Emails().emails_delete_confirmed()

upd_data_90 = Accounts().update_account_info(data_90)
fullness_90 = Accounts().get_profile_fullness(pmid)
print(fullness_90.text)

assert 50 == fullness_50.json()['rate']
assert 90 == fullness_90.json()['rate']