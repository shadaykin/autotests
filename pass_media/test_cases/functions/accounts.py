import requests, json, time
import variables as e
from functions.cookies import Sessions

class Accounts:

	env = e.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)
	link = e.options[env]
	endpoint = e.endpoints_account
	
	def get_account_info(self):
		info = self.session.get(self.link+self.endpoint['edit'])
		return info
		
	def check_restore_password(self):
		if len(args) == 0:
			data = {"password":e.options['password']}
			check = self.session.post(self.link+self.endpoint['check_pwd'],json=data)
		else:
			data = {"password":args[0]}
			check = self.session.post(self.link+self.endpoint['check_pwd'],json=data)
		return check
		
	def change_password(self,*args):
		if len(args) == 1:
			data={"password":args[0],"password_confirm":args[0]}
		if len(args) == 0:
			data={"password":e.options['password'],"password_confirm":e.options['password']}
		if len(args) == 2:
			data={"password":args[0],"password_confirm":args[1]}
		change = self.session.put(self.link+self.endpoint['change_pwd'],json=data)
		return change
		
	def delete_account(self,*args):
		if len(args) == 0:
			password = e.options['password']
		else:
			password = args[0]
		data = {"password":password}
		delete = self.session.delete(self.link+self.endpoint['edit'],json=data)
		return delete
			
