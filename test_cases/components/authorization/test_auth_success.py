import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, json,sys
from functions.clear_cash import Cookie

def test_authorization():
	
	cash=Cookie.clear_cash_func()
	driver =webdriver.Firefox(cash)
	
	#driver.maximize_window()
	
	from functions.authorization import Authorization
	Authorization.correct_authorization(driver)
	assert "accounts/edit" == driver.current_url.split("https://passport.jw-test.zxz.su/")[1], driver.close()
	driver.close()
	
	