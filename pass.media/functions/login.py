from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Data_login():
	
	
	def correct_login(browser):
		enter_login = browser.find_element_by_class_name("phone__number")
		enter_login.clear()
		enter_login.send_keys("9096201687")
		time.sleep(1)
		enter_login.submit()
		
	def incorrect_login(browser):
		enter_login = browser.find_element_by_class_name("phone__number")
		enter_login.clear()
		enter_login.send_keys("00021154")
		time.sleep(1)
		enter_login.submit()
		
		
		