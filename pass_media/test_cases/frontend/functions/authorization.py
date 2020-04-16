import variables as var
from backend.functions.cookies import Sessions
from selenium import webdriver
import time


class Authorization:

    domain = var.options[var.stand_for_test]
    '''Ввод номера телефона в инпут'''
    def set_phone(self, browser, phone, *args):
        phone_num = phone[2:12]
        try:
            if len(args) == 0:
                browser.get(self.domain + '/cas/login/')
            else:
                browser.get(self.domain + '/cas/login/?service=' + args[0])
            time.sleep(0.5)
            phone_input = browser.find_element_by_class_name('phone__number')
            phone_input.send_keys(phone_num)
            time.sleep(1)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            next_button.click()
            time.sleep(1)
            return browser
        except Exception:
            browser.close()
            print("Error enter phone")
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



