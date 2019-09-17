#https://stepik.org/lesson/138920/step/11?unit=196194

from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first_block .form-control.first")
    input1.send_keys("First name")
    input2 = browser.find_element_by_class_name("first_block .form-control.second")
    input2.send_keys("Last name")
    input3 = browser.find_element_by_class_name("first_block .form-control.third")
    input3.send_keys("email")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    time.sleep(1)

    success = browser.find_element_by_tag_name("h1")
    assert success.text == "Congratulations! You have successfully registered!"
finally:

     # закрываем браузер после всех манипуляций
    browser.quit()

 # не забываем оставить пустую строку в конце файла