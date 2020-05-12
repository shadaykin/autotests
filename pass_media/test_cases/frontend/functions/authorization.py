import variables as var
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


class Authorization:

    acc = Accounts()
    domain = var.options[var.stand_for_test]

    def set_browser(self):
        """Выбираем используемый для тестов браузер. Устаналивается в variables"""
        browser = var.browser
        if browser == 'chrome':
            driver = webdriver.Chrome()
            driver.implicitly_wait(5)
        if browser == 'firefox':
            driver = webdriver.Firefox()
            driver.implicitly_wait(5)
        return driver

    def set_phone(self, browser, phone, *args):
        """Ввод номера телефона в инпут и переход на ввод пароля"""
        try:
            if len(args) == 0:
                browser.get(self.domain + '/cas/login/')
            else:
                browser.get(self.domain + '/cas/login/?service=' + args[0])
            time.sleep(1)
            if 'test' in args:
                phone_input = browser.find_element_by_class_name('phone__code')
                phone_num = phone
            else:
                phone_input = browser.find_element_by_class_name('phone__number')
                phone_num = phone[2:12]
            phone_input.clear()
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

    def auth_admin(self, browser):
        """Авторизация в админке"""
        link = self.domain + '/admin/'
        try:
            browser.get(link)
            username = browser.find_element_by_name('username')
            username.send_keys('+79995555555')
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty123')
            password.submit()
            assert browser.current_url == link, "can't authorize"
        except:
            browser.close()
            assert 1 == 2

    def set_cookie(self, browser):
        """Устанавливаем куку с сессией в бразуере"""
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
                    pass
            assert edit
        except:
            print("Can`t add cookie")
            browser.close()
            assert 1 == 2