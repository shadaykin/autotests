import requests, json
from datetime import datetime, timedelta
import data_request as dr
import data_response as d_res
import variables as var
from functions.cookies import Sessions
from functions.emails import Emails
from functions.accounts import Accounts

'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)
'''


#put = Accounts().put_account_education('special_ed')
ed = Accounts().get_account_education()
print(ed.text)
