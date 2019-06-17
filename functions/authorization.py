from selenium import webdriver
import time

class Authorization():

	def correct_authorization(driver):
		# create a new Firefox session
		url='https://passport.jw-test.zxz.su/cas/login'
		
		# Navigate to the application home page
		driver.get(url)
		assert "Pass.Media" in driver.title
		
		from functions.login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)
		
		from functions.password import Data_pwd
		Data_pwd.correct_pwd(driver)
		time.sleep(2)
		
		
		
	def incorrect_authorization(driver):

		url='https://passport.jw-test.zxz.su/cas/login'
		
		# Navigate to the application home page
		driver.get(url)
		
		assert "Pass.Media" in driver.title
		
		from login import Data_login
		Data_login.correct_login(driver)
		time.sleep(1)
		
		
		from password import Data_pwd
		Data_pwd.correct_pwd(driver)
		time.sleep(2)