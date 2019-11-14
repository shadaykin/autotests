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

	"""Проверка на закрытость API под авторизацию""" 
	def test_emails_permission(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code != 403:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API who available without authorization: '+str(fail))
	'''

	"""Добавление неподтвержденного адреса
		Есть есть неподтвержденный email_count = 2"""
		
	def test_add_unconfirmed_email(self):
		if self.e.emails_count() != 0:
			self.e.emails_delete_confirmed()
			self.e.emails_delete_unconfirmed()
			print(self.e.emails_count())
		assert self.e.emails_count() == 0
		self.e.emails_add()
		assert self.e.emails_count() == 2
	'''

	""" Удаление неподтвержденного адреса 
		Добавляем адрес для удаления, если его нет"""
	
	def test_remove_unconfirmed_email(self):
		if len(self.e.emails_unconfirmed_list()) != 0:
			self.e.emails_delete_unconfirmed()
			assert len(self.e.emails_unconfirmed_list()) == 0
		else:
			self.e.emails_add()
			assert len(self.e.emails_unconfirmed_list()) != 0
			self.e.emails_delete_unconfirmed()
			assert len(self.e.emails_unconfirmed_list()) == 0

	""" Удаление подтвержденного адреса """
	def test_remove_confirmed_email(self):
		if len(self.e.emails_confirmed_list()) != 0:
			self.e.emails_delete_confirmed()
			assert len(self.e.emails_confirmed_list()) == 0
	
		#Нужно дописать!!!!!!!!!!!!!!!!!!!!!!!!!
		
	



