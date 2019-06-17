import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, json,sys

sys.path.insert(0, '/autotests/functions')

def test_authorization():
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.delete_all_cookies()
	#driver.maximize_window()
	
	from autotests.functions.authorization import Authorization
	Authorization.correct_authorization(driver)
	