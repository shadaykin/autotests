import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, json,sys
from functions.clear_cash import Cookie
from functions.authorization import Authorization

def test_auth_success():
	

	driver = webdriver.Chrome()
	
	#driver.maximize_window()
	try:
		Authorization.correct_authorization(driver)
		assert "accounts/edit" == driver.current_url.split("https://passport.jw-test.zxz.su/")[1], driver.close()
		driver.close()
	except:
		assert 1 == 2,driver.close()

	
	