import requests, json, time
import variables as e
from selenium import webdriver
from functions.cookies import Sessions
from functions.emails import Emails

env = e.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

Emails().emails_unconfirmed_list()
Emails().emails_delete_unconfirmed()
unconf_emails2 = Emails().emails_unconfirmed_list()
print(unconf_emails2)
"""
for email in unconf_emails:
	data = {"email": email, "confirmed": "false"}
	url = e.options[env]+e.endpoints_email['email_remove']
	print(data)
	print(url)
"""
