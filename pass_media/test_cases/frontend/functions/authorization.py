import variables as var
from backend.functions.cookies import Sessions
from selenium import webdriver
import time


class Authorization:

    domain = var.options[var.stand_for_test]

    def enter_phone_number(self, browser, phone):
        try:
            phone_input = browser.find_element_by_class_name('phone__number')
            phone_input.send_keys(phone)
        except Exception:
            print("Error enter phone")

    def set_phone(self, browser):
        phone = var.options['phone'][2:12]
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(0.5)
            self.enter_phone_number(browser, phone)
            time.sleep(1)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            next_button.click()
            time.sleep(1)
            return browser
        except Exception:
            browser.close()
            assert 1 == 2

    '''Устанавливаем куку с сессией'''

    def set_cookie(self, browser):
        try:
            browser.get(self.domain + '/cas/login/')
            cookie = Sessions().get_sessionid(var.stand_for_test, 1)
            browser.add_cookie(cookie)
            browser.refresh()
            edit = False
            n = 0
            while not edit and n < 5:
                try:
                    assert '/accounts/edit' in browser.current_url
                    edit = True
                except:
                    time.sleep(0.5)
                    n += 1
            assert edit
        except:
            print("Can`t add cookie")
            browser.close()
            assert 1 == 2



