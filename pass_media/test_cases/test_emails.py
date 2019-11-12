import enviroments as env
from functions.params import Session
import requests
import json

class TestEmails:

	obj = Session()
	link = env.options['prod']
	ep = env.endpoints

	cookies = obj.get_sessionid('prod')

	def test_emails_permission(self):
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			print(make_request.status_code)
			if make_request.status_code == 403:
				assert 1 == 2, print(self.ep[endpoint] +' dont have restriction')


	

		






