import enviroments as env
from functions.params import Session as s
import requests


class Emails:


	link = env.options['test']
	ep = env.endpoints
	cookies = s.get_sessionid(link)

	def test_emails_list(self):
		make_request = requests.get(self.link+self.ep['email_list'])
		s_c = make_request.status_code
		return s_c

#object1 = Emails()
#print(object1.emails_list())

