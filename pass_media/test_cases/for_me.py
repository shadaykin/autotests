import requests, json, time
import variables as var
#from frontend.functions.phone import Test
#from functions.cookies import Sessions
from selenium import webdriver
#from functions.emails import Emails
#from functions.accounts import Accounts
#from functions.services import Services
from frontend.functions.authorization import Authorization
from selenium.webdriver.common.keys import Keys
'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

req = session.get('https://passport.test-201.zxz.su/api/cities/autocomplete/')
print(req.text)
'''

browser = webdriver.Chrome()
Authorization().set_cookie(browser)
time.sleep(1)
edit = browser.find_element_by_class_name('link__icon.icon.icon-edit')
edit.click()
time.sleep(1)
gender = browser.find_element_by_css_selector("label[for='genderMale']")
gender.click()
city = browser.find_element_by_css_selector("input[data-vv-as='Город']")
city.send_keys(Keys.CONTROL + "a")
city.send_keys(Keys.DELETE)
city.send_keys('New York')

