import requests, json, time
import variables as e
from selenium import webdriver
from functions.cookies import Sessions

class Profiles:

	env = e.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)

	def get_account_info(self):
		info = requests.get(e.options[env]+)
