import variables as var
from functions.cookies import Sessions
from functions.emails import Emails
import requests, json

class TestEmails:

	stand = var.stand_for_test
	
	s = Sessions()
	e = Emails()
	link = var.options[stand]
	ep = var.endpoints_email
	
	""" Проверка на доступность API  """
	def test_email_available_api(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code >= 500:
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
		Если есть неподтвержденный email_count = 2"""
		
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
			assert remove.status_code == 204
			assert len(self.e.emails_unconfirmed_list()) == 0
		else:
			self.e.emails_add()
			assert len(self.e.emails_unconfirmed_list()) != 0
			remove = self.e.emails_delete_unconfirmed()
			assert remove.status_code == 204
			assert len(self.e.emails_unconfirmed_list()) == 0
	'''
	""" Удаление подтвержденного адреса """
	def test_remove_confirmed_email(self):
		if len(self.e.emails_confirmed_list()) != 0:
			del = self.e.emails_delete_confirmed()
			assert del.status_code == 204
			assert len(self.e.emails_confirmed_list()) == 0 
	
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
		address = var.options['email']
		error = 'User email already exists.'
		if self.e.emails_count() == 0:
			self.e.emails_add()
			assert address in self.e.emails_unconfirmed_list()
			same = self.e.emails_add()
			assert error in same.text
		else:
			self.e.emails_delete_unconfirmed()
			self.e.emails_delete_confirmed()
			self.e.emails_add()
			assert address in self.e.emails_unconfirmed_list()
			same = self.e.emails_add()
			assert error in same.text

	""" Добавление больше 5 адресов """
	def test_excess_email(self):
		error = 'User emails limit exceeded.'
		if self.e.emails_count() == 0:
			for email in var.emails_excess:
				self.e.emails_add(var.emails_excess[email])
			assert len(self.e.emails_unconfirmed_list()[4]) != 0
			fail = self.e.emails_add()
			assert error in fail.text

		if self.e.emails_count() == 2:
			self.e.emails_delete_unconfirmed()
			assert self.e.emails_count() == 0
			for email in var.emails_excess:
				self.e.emails_add(var.emails_excess[email])
			assert len(self.e.emails_unconfirmed_list()[4]) != 0
			fail = self.e.emails_add()
			assert error in fail.text
		else:
			self.e.emails_delete_unconfirmed()
			self.e.emails_delete_confirmed()
			assert self.e.emails_count() == 0
			for email in var.emails_excess:
				self.e.emails_add(var.emails_excess[email])
			assert len(self.e.emails_unconfirmed_list()[4]) != 0
			fail = self.e.emails_add()
			assert error in fail.text

		"""Добавление адреса, который подтвержден у другого пользователя"""
	def test_add_busy_confirmed_email(self):
		error = 'Email already confirmed.'
		if self.e.emails_count() != 0:
			self.e.emails_delete_confirmed()
			self.e.emails_delete_unconfirmed()
		busy = self.e.emails_add(var.options['email_busy'])
		assert error in busy.text
		assert busy.status_code == 400
		
	
