import variables as var
from functions.cookies import Sessions
from functions.accounts import Accounts
from functions.emails import Emails
from functions.services import Services
import data_request as dt
import response_account as resp_acc
import requests, json

class TestAccounts:

	stand = var.stand_for_test
	
	acc = Accounts()
	em = Emails()
	srv = Services()
	link = var.options[stand]
	ep = var.endpoints_account
	
	cookie = Sessions().get_sessionid(stand)
	session = requests.Session()
	session.cookies.update(cookie)
	
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
			if endpoint == 'logout' or endpoint == 'check_phone':
				pass
			else:
				make_request = requests.get(self.link + self.ep[endpoint])
				if make_request.status_code != 403:
					fail.append(self.ep[endpoint])
		if len(fail) != 0:
			assert 1 == 2, print('API who available without authorization: '+str(fail))
	
	def test_update_account_info(self):
		"""Проверка обновления отдельных полей"""
		data = {"first_name": "TEST_name", "nickname": "TEST_nickname"}
		data_clear = {"first_name": "", "nickname": ""}
		self.acc.update_account_info(data_clear)
		info = self.acc.get_account_info().json()	
		assert info['first_name'] == '' and info['nickname'] == ''
		info = self.acc.update_account_info(data).json()
		assert info['first_name'] == 'TEST_name' and info['nickname'] == 'TEST_nickname'
		
	def test_update_all_account_info(self):
		"""Обновеление всех данных пользователя"""
		data_field = dt.account
		data_empty = dt.account_empty
		empty = self.acc.update_all_account_info('empty').json()
		for key in empty.keys():
			if key == 'emails_unconfirmed' or key == 'emails_confirmed' or key == 'password_change_date':
				pass
			else:
				assert data_empty[key] == empty[key]
				
		upd = self.acc.update_all_account_info().json()
		for key in upd.keys():
			if key == 'emails_unconfirmed' or key == 'emails_confirmed' or key == 'password_change_date':
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
		
	def test_account_birthdate(self):
		"""Проверка поля дата рождения"""
		data1 = {"birthdate": "11.01.1910"}
		data2 = {"birthdate": "11.01.2020"}
		data3 = {"birthdate": "11.01.2000"}
		err_more100 = 'Wrong date. Max age: 100.'
		err_less16 = 'You should be over 16 years old.'
		more_100 = self.acc.update_account_info(data1)
		less_16 = self.acc.update_account_info(data2)
		ok = self.acc.update_account_info(data3)
		assert err_more100 in more_100.text
		assert err_less16 in less_16.text
		assert '11.01.2000' == ok.json()['birthdate']

	def test_city_autocomplete(self):
		"""Автокомплит города"""
		msc = 'Москва'
		spb = 'Санкт-Петербург'
		ekb = 'Екатеринбург'
		req_msc = self.session.get(self.link+self.ep['city'],params='q=Мос')
		req_spb = self.session.get(self.link+self.ep['city'],params='q=Санк')
		req_ekb = self.session.get(self.link+self.ep['city'],params='q=Ека')
		moscow = req_msc.json()["results"][0]['full_name']
		piter = req_spb.json()["results"][0]['full_name']
		ekater = req_ekb.json()["results"][0]['full_name']
		assert msc in moscow
		assert spb in piter
		assert ekb in ekater

	def test_delete_educations(self):
		"""Удаление образования пользователя"""
		add = self.acc.add_account_education('higher_ed')
		get = self.acc.get_account_education()
		assert get.json()['level'] != None
		delete = self.acc.delete_account_education()
		assert delete.status_code == 204
		get = self.acc.get_account_education()
		assert get.text == ''

	def test_add_educations(self):
		"""Добавление всех уровней образования поочередно"""
		levels = ['higher_ed','higher_unf_ed','general_ed','general_unf_ed',
				  'special_ed','special_unf_ed']
		for level in levels:
			add = self.acc.add_account_education(level)
			get = self.acc.get_account_education().json()
			exp_response = getattr(resp_acc, level)
			exp_response_inst = exp_response['institutions'][0]
			get_inst = get['institutions'][0]
			assert exp_response['level'] == get['level']
			for key in get_inst.keys():
				if key == 'education' or key == 'id':
					pass
				else:
					assert get_inst[key] == exp_response_inst[key]

	def test_success_check_password(self):
		"""Успешная проверка текущего пароля"""
		body = {"status": "ok", "change_seconds":300}
		check = self.acc.check_restore_password()
		assert check.status_code == 200
		assert check.json() == body

	def test_unsuccessful_check_password(self):
		"""Неуспешная проверка текущего пароля"""
		error = "Wrong current password." 
		check = self.acc.check_restore_password('1111111')
		assert check.status_code == 400
		assert error in check.text

	def test_profile_fullness(self):
		"""Проверка заполненности полей пользователя"""
		pmid = self.srv.get_pmid(self.session)
		field_90 = ['first_name', 'last_name', 'nickname', 'city', 'gender', 'birthdate', 'email']
		field_50 = ['first_name', 'last_name', 'email']

		data_90 = self.acc.generate_account_data(field_90)
		data_50 = self.acc.generate_account_data(field_50)

		self.acc.update_all_account_info('empty')
		self.em.emails_delete_unconfirmed()
		self.em.emails_delete_confirmed()

		self.acc.update_account_info(data_50)
		fullness_50 = self.acc.get_profile_fullness(pmid)

		self.acc.update_all_account_info('empty')
		self.em.emails_delete_unconfirmed()
		self.em.emails_delete_confirmed()
		self.acc.update_account_info(data_90)
		fullness_90 = self.acc.get_profile_fullness(pmid)

		assert 50 == fullness_50.json()['rate']
		assert 90 == fullness_90.json()['rate']
			
	def test_success_change_pwd(self):
		"""Успешная смена пароля"""
		body = {"status": "ok"}
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
		data = {"first_name": "Test_name"}
		error = 'The password is too similar to the first_name'
		self.acc.update_account_info(data)
		self.acc.check_restore_password()
		change = self.acc.change_password(pwd)
		assert change.status_code == 400
		assert error in change.text

	def test_pwd_no_lowercase_letter(self):
		"""Пароль не содержит строчной буквы"""
		pwd = '111111XX'
		error = 'The password must contain at least 1 lowercase letter.'
		self.acc.check_restore_password()
		change = self.acc.change_password(pwd)
		assert change.status_code == 400
		assert error in change.text

	def test_pwd_no_capital_letter(self):
		"""Пароль не содержит заглавной буквы"""
		pwd = '111111xx'
		error = 'The password must contain at least 1 capital letter.'
		self.acc.check_restore_password()
		change = self.acc.change_password(pwd)
		assert change.status_code == 400
		assert error in change.text

	def test_pwd_less_8_characters(self):
		"""Пароль содержит менее 8 символов"""
		pwd = '1111xX'
		error = 'This password is too short. It must contain at least 8 characters.'
		self.acc.check_restore_password()
		change = self.acc.change_password(pwd)
		assert change.status_code == 400
		assert error in change.text


	def test_logout(self):
		"""Логаут пользователя на РМ"""
		info = self.acc.get_account_info()
		assert info.status_code == 200
		logout = self.acc.logout_account()
		assert logout.status_code == 200
		after = self.acc.get_account_info()
		assert after.status_code == 403
		cookie = Sessions().get_sessionid(self.stand)
		self.acc.session.cookies.update(cookie)

	def test_unsuccess_delete_account(self):
		"""Неуспешное удаление пользователя"""
		error = "Wrong password."
		delete = self.acc.delete_account('111111')
		assert delete.status_code == 400
		assert error in delete.text
	
	'''
	def test_success_delete_account(self):
		"""Успешное удаление пользователя"""
		pwd = var.options['password']
		response = resp_acc.check_unreg_phone
		delete = self.acc.delete_account(pwd)
		assert delete.status_code == 200
		check = self.acc.check_phone()
		assert check.json() == response
	'''
	
	def test_auth_phone(self):
		"""Проверка зарегистрированного номера с паролем"""
		response = resp_acc.check_phone
		check = self.acc.check_phone()
		#assert check.status_code == 200
		assert check.json() == response

	def test_auth_phone(self):
		"""Проверка зарегистрированного номера без пароля"""
		phone = var.options['phone_no_pwd']
		response = resp_acc.check_phone_no_pwd
		check = self.acc.check_phone(phone)
		assert check.status_code == 200
		assert check.json() == response

	def test_unreg_phone(self):
		"""Проверка незарегистрированного номера"""
		phone = '%2B80098900077'
		response = resp_acc.check_unreg_phone
		check = self.acc.check_phone(phone)
		assert check.status_code == 200
		assert check.json() == response		

