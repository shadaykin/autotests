import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
import data_tests as dt
import requests, json

class TestAccounts:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	link = var.options[stand]
	ep = var.endpoints_account
	
	def test_accounts_available_api(self):
		"""Проверка доступности API"""
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code >= 500:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API with server errors: '+str(fail))
	
	def test_correct_accounts_fields(self):
		"""Проверка корректной отдачи набора полей аккаунта"""
		account = self.acc.get_account_info().json()
		assert dt.account.keys() == account.keys()
	
	def test_accounts_permission(self):
		"""Проверка закрытости api под авторизацию"""
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code != 403:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API who available without authorization: '+str(fail))
	