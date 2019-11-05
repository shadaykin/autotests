import requests
import enviroments as e
import json


class Session:


	def get_sessionid(self, env):

		link = e.options[env] + '/cas/login'
		s = requests.Session()
		get_csrf = s.get(link)
		csrftoken = get_csrf.cookies['csrftoken']
		cookies = {'csrftoken': csrftoken}
		headers = {'X-CSRFToken': csrftoken, 'Referer': link}
		form_data = {'username': (None, e.options['phone']), 'password': (None, e.options['password'])}
		response = s.post(link, files=form_data, headers=headers, cookies=cookies)
		session_id = {'sessionid': s.cookies['sessionid']}
		return session_id
		
class Emails:
	
	cook = Session()
	cookies = cook.get_sessionid('prod')
	
	def emails_list(self, env, endpoint):
		count = 0
		make_request = requests.get(e.options[env]+e.endpoints[endpoint], cookies=self.cookies)
		st_code = make_request.text
		emails = json.loads(st_code)
		try:
			unconf_emails = emails['unconfirmed_emails'][0]['email']
			count += 1	
		except:
			pass
		try:
			conf_emails = emails['emails']['email']
			count += 2
		except:
			pass
		return count
		
	def delete_conf_email(self):
		conf_emails = self.emails_list('prod','email')
		print(conf_emails)

'''
	def delete_unconf_email(self):
		conf_emails = data_test['emails']
		for email in conf_emails:
			print(email['email'])
'''









