import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import response_service as resp_acc
import variables as var
from functions.cookies import Sessions
from selenium import webdriver
#from functions.emails import Emails
from functions.accounts import Accounts
from functions.services import Services


env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

def pwd_no_lowercase_letter():
	"""Пароль не содержит строчной буквы"""
	pwd = '111111XX'
	error = 'The password is too similar to the first_name'
	Accounts().check_restore_password()
	change = Accounts().change_password(pwd)
	return change
def pwd_no_uppercase_letter():
	"""Пароль не содержит заглавной буквы"""
	pwd = '111111xx'
	error = 'The password is too similar to the first_name'
	Accounts().check_restore_password()
	change = Accounts().change_password(pwd)
	return change
	
def pwd_less_8_characters():
	"""Пароль содержит менее 8 символов"""
	pwd = '111111'
	error = 'The password is too similar to the first_name'
	Accounts().check_restore_password()
	change =Accounts().change_password(pwd)
	return change
	
print(pwd_less_8_characters().text)
print(pwd_no_uppercase_letter().text)
print(pwd_no_lowercase_letter().text)