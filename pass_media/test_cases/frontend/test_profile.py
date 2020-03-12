from frontend.functions.authorization import Authorization
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import variables as var
import time


class TestProfile:

    domain = var.options[var.stand_for_test]
    auth = Authorization()
    acc = Accounts()

    first_name = "first_name"
    last_name = "last_name"
    nickname = "nickname"
    gender = "label[for='genderMale']"
    birthdate = "birthdate"
    city = "input[data-vv-as='Город']"

    '''Выбираем используемый для тестов браузер. Устаналивается в variables'''
    def set_browser(self):
        browser = var.browser
        if browser == 'chrome':
            driver = webdriver.Chrome()
        if browser == 'firefox':
            driver = webdriver.Firefox()
        return driver

    '''Проверка заполнения личных данных в ЛК'''
    def test_welcome(self):
        browser = self.set_browser()
        try:
            browser.get(self.domain + '/cas/login/')
            self.auth.set_cookie(browser)
            time.sleep(1)
            assert browser.current_url == self.domain + '/accounts/edit'
            personal = browser.find_element_by_tag_name('h2')
            assert personal.text == 'Личные данные'
            edit = browser.find_element_by_class_name('link__icon.icon.icon-edit')
            edit.click()
            first_name = browser.find_element_by_id(self.first_name)
            last_name = browser.find_element_by_id(self.last_name)
            nickname = browser.find_element_by_id(self.nickname)
            gender = browser.find_element_by_css_selector(self.gender)
            birthdate = browser.find_element_by_id(self.birthdate)
            city = browser.find_element_by_css_selector(self.city)
            first_name.clear()
            first_name.send_keys('Name test')
            last_name.clear()
            last_name.send_keys('Last name test')
            nickname.clear()
            nickname.send_keys('Nickname test')
            gender.click()
            birthdate.clear()
            birthdate.send_keys('11.01.1999')
            city.send_keys(Keys.CONTROL + "a")
            city.send_keys(Keys.DELETE)
            city.send_keys('New York')
            time.sleep(3)
        except Exception:
            browser.close()
            assert 1 == 2
