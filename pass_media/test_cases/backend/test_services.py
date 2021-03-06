import variables as var
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from backend.functions.services import Services
import backend.response_service as resp_srv
import requests, json


class TestServices:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	srv = Services()
	link = var.options[stand]
	endpoints = var.endpoints_service


	def test_service_available_api(self):
		"""Проверка доступности API"""
		fail = []
		for endpoint in self.endpoints:
			make_request = requests.get(self.link + self.endpoints[endpoint])
			if make_request.status_code >= 500:
				fail.append(self.endpoints[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API with server errors: ' + str(fail))

	def test_service_permission(self):
		"""Проверка закрытости api под авторизацию"""
		fail = []
		for endpoint in self.endpoints:
			if endpoint == ('service_info' or 'app_info'):
				pass
			else:
				make_request = requests.get(self.link + self.endpoints[endpoint])
				if make_request.status_code <= 400 and make_request.status_code >= 500:
					fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API that are available without session: '+str(fail))

	def test_required_fields_cas(self):
		#cookie = Sessions().get_sessionid(self.stand)
		#self.acc.session.cookies.update(cookie)
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
		service = var.options['cas']
		service_info = {"service_name": "AutoTest CAS", "service_branding": False, "service_logo": "", "return_url": "https://localhost111"}
		info = self.srv.get_service_info(service)
		assert info.status_code == 200
		assert service_info == info.json()

	def test_app_info(self):
		"""Проверка отдачи полей по сервисам CAS"""
		service = var.options['oauth_pub']
		link = var.options[var.stand_for_test]
		endpoint = var.endpoints_service['app_info']
		service_info = {"service_name": "AutoTest Oauth Pub",
						"service_logo": "",
						"service_branding": False, "return_url": "https://localhost111"}
		info = requests.get(link+endpoint+service)
		assert info.status_code == 200
		assert service_info == info.json()
	'''
	def test_get_api_key(self):
		"""Проверка передачи данных через api-key"""
		data = resp_srv.api_key
		pmid = self.srv.get_pmid(self.session)
		info = self.srv.get_api_key(pmid)
		assert info.status_code == 200
		tokens = 0
		for key in info.json().keys():
			if key == 'pm_id':
				pass
			elif key == 'access_token' or key == 'refresh_token':
				tokens += 1
			else:
				assert data[key] == info.json()[key]
	'''