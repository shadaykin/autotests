import requests, json, time
import variables as var
from selenium import webdriver
from backend.functions.cookies import Sessions

class Emails:

	env = var.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)

	def emails_list(self):
		make_request = self.session.get(var.options[self.env] + var.endpoints_email['email'])
		st_code = make_request.text
		emails = json.loads(st_code)
		return emails

	def emails_count(self):
		count = 0
		have = self.emails_list()
		try:
			have_conf_email = have['emails'][0]['email']
			count += 1
		except:
			pass
		try:
			have_unconf_email = have['unconfirmed_emails'][0]['email']
			count += 2
		except:
			pass
		return count

	def emails_confirmed_list(self):
		em = self.emails_list()
		conf_email = []
		for email in em['emails']:
			conf_email.append(email['email'])
		return conf_email

	def emails_unconfirmed_list(self):
		em = self.emails_list()
		unconf_email = []
		for email in em['unconfirmed_emails']:
			unconf_email.append(email['email'])
		return unconf_email
	
	def emails_delete_unconfirmed(self, *args):
		del_request = ''
		if len(args) > 0:
			if "@" in args[0]:
				data = {"email": args[0], "confirmed": "false"}
				url = var.options[self.env]+var.endpoints_email['email_remove']
				del_request = self.session.delete(url, json=data)
			else:
				assert 1 == 2, "Args is not email"
		unconf_emails = self.emails_unconfirmed_list()
		for email in unconf_emails:
			data = {"email": email, "confirmed": "false"}
			url = var.options[self.env]+var.endpoints_email['email_remove']
			del_request = self.session.delete(url, json=data)
		return del_request

	def emails_delete_confirmed(self):
		del_request = ''
		conf_emails = self.emails_confirmed_list()
		for email in conf_emails:
			data = {"email": email, "confirmed": "true", "password": e.options['password']}
			url = var.options[self.env] + var.endpoints_email['email_remove']
			del_request = self.session.delete(url, json=data)
		return del_request
		
	def emails_add(self, *args):
		try:
			'@' in args[0]
			link = var.options[self.env]+var.endpoints_email['email']
			data = {'email': args[0]}
			add_request = self.session.post(link, json=data)
			return add_request
		except:
			link = var.options[self.env]+var.endpoints_email['email']
			data = {'email': var.options['email']}
			add_request = self.session.post(link, json=data)
			return add_request

	
	"""Подтверждение адреса с помощью кода"""
	def emails_confirm_key(self, email, code):
		endpoint = var.endpoints_email['email_confirm']
		data={"email": email, "confirmation_key": code}
		confirm = self.session.post(var.options[self.env]+endpoint, data=data)
		return confirm



