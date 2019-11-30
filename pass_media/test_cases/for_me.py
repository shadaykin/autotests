import requests, json, time
import variables as e
from selenium import webdriver
from functions.cookies import Sessions
from functions.emails import Emails

var = e.stand_for_test

cookie = Sessions().get_sessionid(var)
session = requests.Session()
session.cookies.update(cookie)

Emails().emails_unconfirmed_list()
delete = Emails().emails_delete_unconfirmed()
unconf_emails2 = Emails().emails_unconfirmed_list()
print(unconf_emails2)
print(delete.status_code)
'''

def qq():
	data = {}
	for i in range(2):
		req = requests.get('https://ya.ru')
	return req
	
print(qq().status_code)
'''

