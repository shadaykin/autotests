import enviroments as env
from functions.params import Session as s
import requests
import json

class TestEmails:

	link = env.options['prod']
	ep = env.endpoints
	cookies = s.get_sessionid('prod')

	def test_emails_permission(self):
		make_request_200 = requests.get(self.link+self.ep['email'],cookies=self.cookies)
		make_request_403 = requests.get(self.link+self.ep['email'])
		success = make_request_200.status_code
		denied = make_request_403.status_code	
		assert success == 200
		assert denied == 403
	
	def test_emails_add(self):
		email_list = requests.get(self.link+self.ep['email'], cookies=self.cookies)
		json_parse = email_list.json()
		empty = False

		try:
			email_conf = json_parse['emails']
			email_unconf = json_parse['unconfirmed_emails']
			print(email_unconf)
			assert len(email_conf) == 0
			assert len(email_unconf) == 0
		except:
			assert 1 == 2







