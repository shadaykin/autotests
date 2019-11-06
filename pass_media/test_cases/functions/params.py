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


	def emails_list(self, env, *args):
		cookies = self.cook.get_sessionid(env)
		make_request = requests.get(e.options[env] + e.endpoints['email'], cookies=cookies)
		st_code = make_request.text
		emails = json.loads(st_code)
		return emails

	def emails_confirmed_list(self, env):
		em = self.emails_list(env)
		conf_email = []
		for email in em['emails']:
			conf_email.append(email['email'])
		return conf_email

	def emails_unconfirmed_list(self, env):
		em = self.emails_list(env)
		unconf_email = []
		for email in em['unconfirmed_emails']:
			unconf_email.append(email['email'])
		return unconf_email








