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

    def set_cookie(self, browser):
        try:
            browser.get(self.domain + '/cas/login/')
            cookie = Sessions().get_sessionid(var.stand_for_test, 1)
            browser.add_cookie(cookie)
            browser.refresh()
        except Exception:
            print("Can`t add cookie")

