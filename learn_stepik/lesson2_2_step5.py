
import time, math
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"


def func(x):
    res = math.log(abs(12*math.sin(int(x))))
    return str(res)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    y = func(x.text)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    r_r = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", r_r)
    r_r.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

   # submit = browser.find_element_by_tag_name("button")
   # submit.click()

finally:
    time.sleep(5)
    browser.quit()
    print("SUCCESS")