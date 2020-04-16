from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random




browser = webdriver.Chrome()

browser.get('https://passport.test-201.zxz.su/cas/login')
time.sleep(2)
phone_input = browser.find_element_by_class_name('phone__number')
code = browser.find_element_by_class_name('phone__code')
phone_input.clear()
code.clear()

code.send_keys('%2B800')
time.sleep(2)
#code.send_keys('111')
time.sleep(4)
browser.close()