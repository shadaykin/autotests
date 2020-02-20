import variables as var
from selenium import webdriver
import time

class Authorization:
    browser = webdriver.Chrome()
    domain = var.options[var.stand_for_test]
    phone = var.options['phone'][2:12]

    def phone_number(self):
        try:
            self.browser.get(self.domain+'/cas/login/')
            time.sleep(1)
            print(self.browser.title)
            assert self.browser.title == 'Pass.Media – единый аккаунт для вселенной развлекательных сервисов'
            next_button = self.browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" in status_btn
            phone_input = self.browser.find_element_by_class_name('phone__number')
            phone_input.send_keys(self.phone)
            next_button.click()
            time.sleep(2)

            self.browser.close()
        except:
            self.browser.close()
            assert 1 == 2