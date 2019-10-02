
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(num1.text)+int(num2.text)))
    time.sleep(1)

    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    time.sleep(3)
    browser.quit()
    print("SUCCESS")