from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random

group1 = ['org-42', 'org-11', 'org-30']
group2 = ['org-57']
group3 = ['org-85','org-95','org-75']
group4 = ['org-115','org-105','org-124','org-113']
group5 = ['org-152','org-149','org-143','org-132']

for i in range(50):
    browser = webdriver.Chrome()
    browser.minimize_window()
    browser.get('https://akr.gppc.ru/lk/poll')
    two = browser.find_element_by_css_selector("input[type='radio'][id='org-57']")
    browser.execute_script('arguments[0].scrollIntoView(true);', two)
    browser.execute_script("arguments[0].click();", two)
    '''
    one = browser.find_element_by_css_selector("input[type='radio'][id='"+random.choice(group1)+"']")
    browser.execute_script('arguments[0].scrollIntoView(true);', one)
    browser.execute_script("arguments[0].click();", one)

    three = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group3) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', three)
    browser.execute_script("arguments[0].click();", three)

    four = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group4) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', four)
    browser.execute_script("arguments[0].click();", four)

    five = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group5) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', five)
    browser.execute_script("arguments[0].click();", five)
    '''
    #go = browser.find_element_by_class_name('btn.btn-lg.btn-primary')
    #go.click()

    browser.find_element_by_class_name('btn.btn-lg.btn-primary').submit()
    browser.close()
    time.sleep(2)