import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
from functions.services import Services
import response_service as resp_srv
import requests, json


class TestServices:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	srv = Services()
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

	def test_service_info_cas(self):
		"""Проверка отдачи полей по сервисам CAS"""
		cookie = Sessions().get_sessionid(self.stand)
		Services().session.cookies.update(cookie)
		service = var.options['cas']
		service_info = {"service_name": "AutoTest CAS", "service_branding": False, "service_logo": "", "return_url": "https://localhost111"}
		info = self.srv.get_service_info(service)
		assert info.status_code == 200
		assert service_info == info.json()
	'''
	def test_get_api_key(self):
		"""Проверка передачи данных через api-key"""
		data = resp_srv.api_key
		pmid = self.srv.get_pmid(self.session)
		info = self.srv.get_api_key(pmid)
		assert info.status_code == 200
		for key in info.json().keys():
			if key == 'pm_id':
				pass
			else:
				assert data[key] == info.json()[key]
	'''