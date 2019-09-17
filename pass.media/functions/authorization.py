import time
from selenium import webdriver

class Authorization():
	
	url = 'https://passport.jw-test.zxz.su/'

	def correct_authorization(driver):
		# create a new Firefox session
		Authorization.url += 'cas/login/'
		
		# Navigate to the application home page
		driver.get(Authorization.url)
		assert "Pass.Media" in driver.title
		
		from functions.login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)
		
		from functions.password import Data_pwd
		Data_pwd.correct_pwd(driver)
		time.sleep(3)
		return Authorization.url
		
		
	def incorrect_authorization(driver):

		Authorization.url+='cas/login/'
		driver.get(Authorization.url)
		
		assert "Pass.Media" in driver.title
		
		from functions.login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)
		
		from functions.password import Data_pwd
		Data_pwd.incorrect_pwd(driver)
		time.sleep(3)
		return Authorization.url
		
	def correct_auth_cas(driver, service):
		url='https://passport.jw-test.zxz.su/cas/login/?service='+str(service)
		driver.get(url)
		assert "Pass.Media" in driver.title
		
		from functions.login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)
		
		from functions.password import Data_pwd
		Data_pwd.correct_pwd(driver)
		time.sleep(3)

	def correct_auth_oauth(driver, client_id, redirect_uri):

		add_url = 'oauth/authorize?'
		driver.get(Authorization.url + add_url + 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri)
		time.sleep(1)

		from functions.login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)

		from functions.password import Data_pwd
		Data_pwd.correct_pwd(driver)
		time.sleep(2)

		driver.find_element_by_xpath("//button[text()='Продолжить']").click()

		try:
			code = driver.current_url.split("code=")[1]
			return code
		except:
			print('Access denied')