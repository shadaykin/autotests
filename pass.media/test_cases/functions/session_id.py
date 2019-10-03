from selenium import webdriver
import time

link = 'https://passport.jw-test.zxz.su/cas/login'

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
code = 0

import pass.mediaenviroments
print(enviroments.options)

try:
    driver.get(link)
    time.sleep(1)
    while code == 0:
        try:
            ph_code = driver.find_element_by_xpath("//input[@name='phone']").get_attribute("value")
            if ph_code == "+7":
                code = 1
                time.sleep(1)
        except:
            assert 1 == 2, "NOT FIND PHONE CODE"

    phone = driver.find_element_by_css_selector(".form-input.phone .phone__number")
    phone.clear()
    phone.send_keys("9067240288")
    time.sleep(1)

    btn_log = driver.find_element_by_tag_name("button").click()
    time.sleep(1)

    pwd = driver.find_element_by_xpath("//input[@name='password']")
    pwd.send_keys("pwd")
    driver.quit()
except:
    assert 1 == 2, driver.quit()
