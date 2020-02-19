import requests, json, time
import variables as e
from selenium import webdriver
from backend.functions.cookies import Sessions

class Emails:

	env = e.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)

	def emails_list(self):
		make_request = self.session.get(e.options[self.env] + e.endpoints_email['email'])
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
				url = e.options[self.env]+e.endpoints_email['email_remove']
				del_request = self.session.delete(url, json=data)
			else:
				assert 1 == 2, "Args is not email"
		unconf_emails = self.emails_unconfirmed_list()
		for email in unconf_emails:
			data = {"email": email, "confirmed": "false"}
			url = e.options[self.env]+e.endpoints_email['email_remove']
			del_request = self.session.delete(url, json=data)
		return del_request

	def emails_delete_confirmed(self):
		del_request = ''
		conf_emails = self.emails_confirmed_list()
		for email in conf_emails:
			data = {"email": email, "confirmed": "true", "password": e.options['password']}
			url = e.options[self.env] + e.endpoints_email['email_remove']
			del_request = self.session.delete(url, json=data)
		return del_request
		
	def emails_add(self, *args):
		try:
			'@' in args[0]
			link = e.options[self.env]+e.endpoints_email['email']
			data = {'email': args[0]}
			add_request = self.session.post(link, json=data)
			return add_request
		except:
			link = e.options[self.env]+e.endpoints_email['email']
			data = {'email': e.options['email']}
			add_request = self.session.post(link, json=data)
			return add_request

	
		
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





