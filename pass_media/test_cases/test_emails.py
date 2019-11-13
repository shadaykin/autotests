import enviroments as env
from functions.params import Session
from functions.params import Emails
import requests
import json

class TestEmails:

	stand = 'prod'
	
	s = Session()
	e = Emails()
	link = env.options[stand]
	ep = env.endpoints

	cookies = s.get_sessionid(stand)
	
	"""Проверка на закрытость API под авторизацию""" 
	def test_emails_permission(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code != 403:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1==2, print('API who available without authorization: '+str(fail))
			
	"""Добавление неподтвержденного адреса"""
	def test_add_unconfirmed_email(self):
		self.e.delete_confirmed_emails(self.stand, self.cookies)
		self.e.delete_unconfirmed_emails(self.stand, self.cookies)
		assert self.e.emails_count(self.stand, self.cookies) == 0
		self.e.add_emails(self.stand, self.cookies)
		assert self.e.emails_count(self.stand, self.cookies) == 2

		





