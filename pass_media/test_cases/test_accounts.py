import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
import requests, json

class TestAccounts:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	link = var.options[stand]
	ep = var.endpoints_account
	
	def test_accounts_available_api(self):
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code >= 500:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API with server errors: '+str(fail))