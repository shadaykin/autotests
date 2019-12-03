import requests, json, time
#import data_tests as dt
import data_tests
import variables as var
from functions.cookies import Sessions
from functions.emails import Emails
from functions.accounts import Accounts


env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

ff = Accounts().get_account_info()
first_name = 'TEST_name'

if ff.json()['first_name'] != first_name:
	print('success')
print(ff.json()['first_name'])
