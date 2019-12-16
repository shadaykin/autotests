import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
import requests, json


class TestServices:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	link = var.options[stand]
	ep = var.endpoints_account

	def test_required_fields_cas(self):
		"""Обязательные поля для сервисов CAS"""
		service = var.options['cas']
		req_fields = ['emails_unconfirmed', 'first_name', 'last_name', 'phone']
		info = self.acc.get_account_info(service)
		required = info.json()['required_fields']
		for req in range(len(required)):
			assert required[req] in req_fields

	def test_optional_fields_cas(self):
		"""Опциональные поля для сервисов CAS"""
		service = var.options['cas']
		opt_fields = ['gender', 'nickname']
		info = self.acc.get_account_info(service)
		optional = info.json()['optional_fields']
		for opt in range(len(optional)):
			assert optional[opt] in opt_fields
	
	def test_required_fields_oauth_pub(self):
		"""Обязательные поля для сервисов OAuth Public"""
		client_id = var.options['oauth_pub']
		req_fields = ['emails_unconfirmed', 'first_name', 'last_name', 'phone']
		info = self.acc.get_account_info(client_id)
		required = info.json()['required_fields']
		for req in range(len(required)):
			assert required[req] in req_fields
	
	def test_optional_fields_oauth_pub(self):
		"""Опциональные поля для сервисов OAuth Public"""
		client_id = var.options['oauth_pub']
		opt_fields = ['gender', 'nickname']
		info = self.acc.get_account_info(client_id)
		optional = info.json()['optional_fields']
		for opt in range(len(optional)):
			assert optional[opt] in opt_fields
