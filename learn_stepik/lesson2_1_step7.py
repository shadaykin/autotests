
import math
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    tresure = browser.find_element_by_id("treasure")
    tresure_value = tresure.get_attribute("valuex")
    y = calc(tresure_value)
    print(y)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()

    robot_check = browser.find_element_by_id("robotCheckbox")
    robot_check.click()

    time.sleep(1)

    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    time.sleep(3)
    browser.quit()
    print("SUCCESS")