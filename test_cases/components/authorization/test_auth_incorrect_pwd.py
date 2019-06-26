import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, json,sys
from functions.clear_cash import Cookie
from functions.authorization import Authorization


def test_incorrect_pwd():

	cash = Cookie.clear_cash_func()
	driver = webdriver.Firefox(cash)
	
	#driver.maximize_window()
	try:
		Authorization.incorrect_authorization(driver)
		assert "cas/login/" == driver.current_url.split("https://passport.jw-test.zxz.su/")[1], driver.close()
		try:
			inc_pwd = driver.find_element_by_class_name('form-message.error')
		except:
			assert 1 == 2, driver.close()
		driver.close()
	except:
		assert 1 == 2, driver.close()