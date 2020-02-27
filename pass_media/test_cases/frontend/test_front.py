from frontend.functions.authorization import Authorization
from backend.functions.cookies import Sessions
from selenium import webdriver
import variables as var
import time


class Test:

    domain = var.options[var.stand_for_test]
    auth = Authorization()
    browser = 'Chrome()'

    def test_welcome(self):
        browser = webdriver.
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(2)
            print(browser.title)
            assert browser.title == 'Pass.Media – единый аккаунт для вселенной развлекательных сервисов'
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" in status_btn
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_enter_phone(self, browser):
        phone = var.options['phone'][2:12]
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(2)
            enter = self.auth.enter_phone_number(browser, phone)
            time.sleep(2)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" not in status_btn, "button is dasabled!"
        except Exception:
            browser.close()
            assert 1 == 2
    '''
    def test_cookie(self):
        try:
            browser = webdriver.Chrome()
            self.auth.set_cookie()
    '''