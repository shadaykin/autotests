from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random

group1 = ['org-42', 'org-11', 'org-30']
group2 = ['org-57']
group3 = ['org-85','org-95','org-75']
group4 = ['org-115','org-105','org-124','org-113']
group5 = ['org-152','org-149','org-143','org-132']

for i in range(10):
    browser = webdriver.Chrome()
    browser.get('https://akr.gppc.ru/lk/poll')
    two = browser.find_element_by_css_selector("input[type='radio'][id='org-57']")
    browser.execute_script('arguments[0].scrollIntoView(true);', two)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", two)
    '''    
    one = browser.find_element_by_css_selector("input[type='radio'][id='"+random.choice(group1)+"']")
    browser.execute_script('arguments[0].scrollIntoView(true);', one)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", one)

    three = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group3) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', three)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", three)

    four = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group4) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', four)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", four)

    five = browser.find_element_by_css_selector("input[type='radio'][id='" + random.choice(group5) + "']")
    browser.execute_script('arguments[0].scrollIntoView(true);', five)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", five)

    go = browser.find_element_by_class_name('btn.btn-lg.btn-primary')
    go.click()
    '''
    browser.find_element_by_class_name('btn.btn-lg.btn-primary').submit()
    browser.close()