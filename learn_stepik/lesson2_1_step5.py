
import math
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_el = browser.find_element_by_id("input_value")
    y = calc(x_el.text)
    print(y)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    robots_rule = browser.find_element_by_css_selector('[for="robotsRule"]')
    robots_rule.click()

    robot_check = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robot_check.click()

    time.sleep(1)

    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    time.sleep(1)
    browser.quit()
    print("SUCCESS")