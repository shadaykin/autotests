import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
import data_tests as dt
import requests, json

class TestServices:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	link = var.options[stand]
	ep = var.endpoints_account


	def test_required_fields_cas(self):
		"""Обязательные поля для сервисов CAS"""
		service='https://matchtv.ru'
		req_fields = ['emails_unconfirmed', 'gender', 'nickname', 'phone']
		info = self.acc.get_account_info(service)
		required = 	info.json()['required_fields']
		assert req_fields == required
		
	
	def test_required_fields_oauth(self):
		"""Обязательные поля для сервисов OAuth"""
		client_id=''
		req_fields = ['emails_unconfirmed', 'gender', 'nickname', 'phone']
		info = self.acc.get_account_info(client_id)
		required = 	info.json()['required_fields']
		assert req_fields == required
	
	def test_optional_fields_cas(self):
		"""Обязательные поля для сервисов CAS"""
		service='https://matchtv.ru'
		opt_fields = ['emails_unconfirmed', 'gender', 'nickname', 'phone']
		info = self.acc.get_account_info(service)
		optional = 	info.json()['optional_fields']
		assert opt_fields == optional
		
	
	def test_optional_fields_oauth(self):
		"""Обязательные поля для сервисов OAuth"""
		client_id=''
		opt_fields = ['emails_unconfirmed', 'gender', 'nickname', 'phone']
		info = self.acc.get_account_info(client_id)
		optional = 	info.json()['optional_fields']
		assert opt_fields == optional
	