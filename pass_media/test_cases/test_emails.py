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
	
	""" Проверка на доступность API  """
	def test_email_available_api(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code >= 500 :
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API with server errors: '+str(fail))
	
	"""Проверка на закрытость API под авторизацию""" 
	def test_emails_permission(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code != 403:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API who available without authorization: '+str(fail))
	

	"""Добавление неподтвержденного адреса
		Есть есть неподтвержденный email_count = 2"""
		
	def test_add_unconfirmed_email(self):
		if self.e.emails_count() != 0:
			self.e.emails_delete_confirmed()
			self.e.emails_delete_unconfirmed()
		assert self.e.emails_count() == 0
		add = self.e.emails_add()
		assert add.status_code == 201
		assert self.e.emails_count() == 2
	

	""" Удаление неподтвержденного адреса 
		Добавляем адрес для удаления, если его нет"""
	
	def test_remove_unconfirmed_email(self):
		unc_list = self.e.emails_unconfirmed_list()
		
		if len(unc_list) != 0:
			remove = self.e.emails_delete_unconfirmed()
			assert remove.status_code >= 200 and remove.status_code < 210
			assert len(self.e.emails_unconfirmed_list()) == 0
		else:
			self.e.emails_add()
			assert len(self.e.emails_unconfirmed_list()) != 0
			remove = self.e.emails_delete_unconfirmed()
			assert remove.status_code >= 200 and remove.status_code < 210
			assert len(self.e.emails_unconfirmed_list()) == 0
	'''
	""" Удаление подтвержденного адреса """
	def test_remove_confirmed_email(self):
		if len(self.e.emails_confirmed_list()) != 0:
			self.e.emails_delete_confirmed()
			assert e.emails_delete_confirmed().status_code == '200'
			assert len(self.e.emails_confirmed_list()) == 0
	
		#Нужно дописать!!!!!!!!!!!!!!!!!!!!!!!!!
	'''
	""" Удаление невалидного адреса """
	def test_remove_invalid_email(self):
		invalid = 'email@email'
		error = 'Enter a valid email address.'
		rm = self.e.emails_delete_unconfirmed(invalid)
		assert error in rm.text 
	
	""" Удаление неподтвержденного
		адреса, которого у пользователя """
	def test_remove_missing_email(self):
		missing_em = 'email@email.ru'
		error = 'User email not found'
		rm = self.e.emails_delete_unconfirmed(missing_em)
		assert error in rm.text 		
	
	""" Добавление одинаковых адресов """	
	def test_same_email(self):
		address = self.env.options['email']
		error = 'Email alredy exists.'
		if self.e.emails_count() == 0:
			self.e.emails_add()
			assert address in self.e.emails_unconfirmed_list()
			same = self.e.emails_add()
			assert error in same.text
		else:
			self.emails_delete_unconfirmed()
			self.emails_delete_confirmed()
			self.e.emails_add()
			assert address in self.e.emails_unconfirmed_list()
			same = self.e.emails_add()
			assert error in same.text

