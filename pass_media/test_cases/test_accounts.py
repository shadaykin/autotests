import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
import data_tests as dt
import requests, json

class TestAccounts:

	stand = var.stand_for_test
	
	s = Sessions()
	acc = Accounts()
	link = var.options[stand]
	ep = var.endpoints_account
	
	def test_accounts_available_api(self):
		"""Проверка доступности API"""
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code >= 500:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API with server errors: '+str(fail))
	
	def test_correct_accounts_fields(self):
		"""Проверка корректной отдачи набора полей аккаунта"""
		account = self.acc.get_account_info().json()
		assert dt.account.keys() == account.keys()
	
	def test_accounts_permission(self):
		"""Проверка закрытости api под авторизацию"""
		fail = []
		for endpoint in self.ep:
			make_request = requests.get(self.link + self.ep[endpoint])
			if make_request.status_code != 403:
				fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API who available without authorization: '+str(fail))
	
	def test_update_account_info(self):
		"""Проверка обновления отдельных полей"""
		first_name = 'TEST_name'
		nickname = 'TEST_nickname'
		info = self.acc.get_account_info()
		if info.json()['first_name'] != first_name and info.json()['nickname'] != nickname:
			self.acc.update_account_info(first_name, nickname)
		else:
			self.acc.update_account_info('','')
			info = self.acc.get_account_info().json()
			assert info['first_name'] != first_name
			assert info['nickname'] != nickname
			self.acc.update_account_info(first_name, nickname)
		info = self.acc.get_account_info().json()	
		assert info['first_name'] == first_name
		assert info['nickname'] == nickname
		
	def test_update_all_account_info(self):
		"""Обновеление всех данных пользователя"""
		data_field = dt.account
		data_empty = dt.account_empty
		#empty = self.acc.get_account_info().json()
		empty = self.acc.update_all_account_info('empty').json()
		for key in empty.keys():
			if key == ('emails_unconfirmed' or 'emails_confirmed'):
				pass
			else:
				assert data_empty[key] == empty[key]
				
		upd = self.acc.update_all_account_info().json()
		for key in upd.keys():
			if key == ('emails_unconfirmed' or 'emails_confirmed'):
				pass
			else:
				assert data_field[key] == upd[key]
	'''				
	def test_mate_field(self):
		"""Проверка ограничений на мат"""
		first_name = 'Блядь'
		nickname = 'Хуй'
		self.acc.update_account_info(first_name, nickname)
	'''	
	
	def test_required_fields_cas(self):
		"""Обязательные поля для сервисов CAS"""
		service='https://localhost'
		req_fields = 'emails_unconfirmed', 'gender', 'nickname', 'phone'
		info = self.acc.get_account_info(service)
		required = 	info.json()['required_fields']
		
	
	
	def test_success_check_password(self):
		"""Успешная проверка текущего пароля"""
		body = {"status":"ok","change_seconds":300} 
		check = self.acc.check_restore_password()
		assert check.status_code == 200
		assert check.json() == body
			
	def test_unsuccessful_check_password(self):
		"""Неуспешная проверка текущего пароля"""
		error = "Wrong current password." 
		check = self.acc.check_restore_password('1111111')
		assert check.status_code == 400
		assert error in check.text 
			
	def test_success_change_pwd(self):
		"""Успешная смена пароля"""
		body = {"status":"ok"}
		self.acc.check_restore_password()
		change = self.acc.change_password()
		assert change.status_code == 200
		assert change.json() == body
		
	def test_change_differents_pwd(self):
		"""Несовпадающие пароли"""
		pwd1 = '111111cC'
		pwd2 = '111111zZ'
		error = 'Passwords not equal.'
		change = self.acc.change_password(pwd1,pwd2)
		assert change.status_code == 400
		assert error in change.text
	
	def test_pwd_have_account_data(self):
		"""Пароль содержит данные профиля"""
		pwd = 'Test_name1'
		error = 'The password is too similar to the first_name'
		self.acc.update_account_info('Test_name')
		self.acc.check_restore_password()
		change = self.acc.change_password(pwd)
		assert change.status_code == 400
		assert error in change.text