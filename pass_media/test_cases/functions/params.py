import requests
import enviroments as e
import json
from selenium import webdriver
import time

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

	env = 'prod'

	cookie = Session().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)

	def emails_list(self):
		make_request = self.session.get(e.options[self.env] + e.endpoints['email'])
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
		try:
			if "@" in args[0]:
				data = {"email": args[0], "confirmed": "false"}
				url = e.options[self.env]+e.endpoints['email_delete']
				del_request = self.session.delete(url, json=data)
		except:
			unconf_emails = self.emails_unconfirmed_list()
			for i in range(len(unconf_emails)):
				email = unconf_emails[i]
				data = {"email": email, "confirmed": "false"}
				url = e.options[self.env]+e.endpoints['email_delete']
				del_request = self.session.delete(url, json=data)
		return del_request

	def emails_delete_confirmed(self):
		conf_emails = self.emails_confirmed_list()
		for i in range(len(conf_emails)):
			email = conf_emails[i]
			data = {"email": email, "confirmed": "true","password":e.options['password']}
			url = e.options[self.env] + e.endpoints['email_delete']
			del_request = self.session.delete(url, json=data)
			
	def emails_add(self):
		link = e.options[self.env]+e.endpoints['email']
		print(link)
		data = {'email': e.options['email']}
		add_request = self.session.post(link, json=data)
		print(add_request.status_code)
		#assert add_request.status_code == 200, 'Error add email'

	def emails_confirm(self):
		browser = webdriver.Chrome()
		link = 'https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https://mail.yandex.ru/?uid=121104012&backpath=https://mail.yandex.ru?noretpath=1'
		browser.get(link)
		email = browser.find_element_by_id('passp-field-login')
		email.send_keys(e.options['email'])
		enter = browser.find_element_by_tag_name('button')
		enter.submit()
		time.sleep(1)
		pwd = browser.find_element_by_id('passp-field-passwd')
		pwd.send_keys(e.options['password'])
		enter = browser.find_element_by_css_selector('.passp-button.passp-sign-in-button button')
		enter.submit()
		mail_pm = browser.find_element_by_css_selector(".ns-view-container-desc.mail-MessagesList.js-messages-list [title='no-reply@pass.media']")
		time.sleep(5)





