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

	cook = Session()

	def emails_list(self, env):
		cookies = self.cook.get_sessionid(env)
		make_request = requests.get(e.options[env] + e.endpoints['email'], cookies=cookies)
		st_code = make_request.text
		emails = json.loads(st_code)
		return emails

	def emails_count(self, env):
		count = 0
		have = self.emails_list(env)
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
	
	def delete_unconfirmed_emails(self, env):
		cookies = self.cook.get_sessionid(env)
		unconf_emails = self.emails_unconfirmed_list(env)
		for i in range(len(unconf_emails)):
			email = unconf_emails[i]
			data = {"email": email, "confirmed": "false"}
			url1 = e.options[env]+e.endpoints['email_delete']
			del_request = requests.delete(url1, json=data, cookies=cookies)

	def delete_confirmed_emails(self, env):
		cookies = self.cook.get_sessionid(env)
		conf_emails = self.emails_confirmed_list(env)
		for i in range(len(conf_emails)):
			email = conf_emails[i]
			data = {"email": email, "confirmed": "true","password":e.options['password']}
			url1 = e.options[env] + e.endpoints['email_delete']
			del_request = requests.delete(url1, json=data, cookies=cookies)
			
	def add_emails(self, env):
		cookies = self.cook.get_sessionid(env)
		link = e.options[env]+e.endpoints['email']
		print(link)
		data = {'email': e.options['email']}
		add_request = requests.post(link, json=data, cookies=cookies)

	def confirm_emails(self):
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





