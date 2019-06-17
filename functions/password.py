from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Data_pwd():
	
		
	def correct_pwd(browser):
		enter_pwd = browser.find_element_by_name("password")
		enter_pwd.clear()
		enter_pwd.send_keys("258963Il")
		time.sleep(1)
		enter_pwd.submit()
		
	def incorrect_pwd(browser):
		enter_pwd = browser.find_element_by_name("password")
		enter_pwd.clear()
		enter_pwd.send_keys("j2e2NNNNa2D")
		time.sleep(1)
		enter_pwd.submit()