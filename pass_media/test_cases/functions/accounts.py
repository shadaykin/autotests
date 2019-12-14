import requests, json, time
import variables as var
import data_request as dr
from functions.cookies import Sessions

class Accounts:

	env = var.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)
	link = var.options[env]
	endpoint = var.endpoints_account
	
	def get_account_info(self, *args):
		#Получение данных по профилю
		if len(args) == 0:
			info = self.session.get(self.link+self.endpoint['edit'])
		else:
			service = args[0]
			if 'http' in args[0]:
				info = self.session.get(self.link+self.endpoint['edit']+'?service='+service)
			else:
				info = self.session.get(self.link+self.endpoint['edit']+'?clientid='+service)
		return info
		
	def update_account_info(self, *args):
		#Обновление конкретных полей
		if len(args) == 1:
			data = args[0]
			patch = self.session.patch(self.link+self.endpoint['edit'],json=data)
			return patch
		else:
			assert 1 == 2, 'Dont have data'
			
	def update_all_account_info(self, *args):
		#Обновление всех данных профиля
		if len(args) == 1:
			data = dr.account_empty
			put = self.session.put(self.link+self.endpoint['edit'],json=data)
			return put
		else:
			data = dr.account
			put = self.session.put(self.link+self.endpoint['edit'],json=data)
			return put
			
	def check_restore_password(self,*args):
		#Проверка текущего пароля/кода восстановления
		if len(args) == 0:
			data = {"password":var.options['password']}
			check = self.session.post(self.link+self.endpoint['check_pwd'],json=data)
		else:
			data = {"password":args[0]}
			check = self.session.post(self.link+self.endpoint['check_pwd'],json=data)
		return check
		
	def change_password(self, *args):
		#Смена пароля
		if len(args) == 1:
			data={"password":args[0],"password_confirm":args[0]}
		if len(args) == 0:
			data={"password":var.options['password'],"password_confirm":var.options['password']}
		if len(args) == 2:
			data={"password":args[0],"password_confirm":args[1]}
		change = self.session.put(self.link+self.endpoint['change_pwd'],json=data)
		return change
		
	def delete_account(self, *args):
		#Удаление профиля пользователя
		if len(args) == 0:
			password = var.options['password']
		else:
			password = args[0]
		data = {"password":password}
		delete = self.session.delete(self.link+self.endpoint['edit'],json=data)
		return delete
	
	def get_account_education(self):
		#Получение данных по образованию пользователя
		education = self.session.get(self.link+self.endpoint['ed'])
		return education
	
	def delete_account_education(self):
		#Удаление образования
		del_education = self.session.delete(self.link+self.endpoint['ed'])
		return del_education
	
	def add_account_education(self,level):
		#Добавление информации по образованию"
		data = getattr(dr, level)
		add_ed = self.session.put(self.link+self.endpoint['ed'],json=data)
		return add_ed