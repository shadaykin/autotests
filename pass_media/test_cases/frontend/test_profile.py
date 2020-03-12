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


    first_name = 'Name test'
    last_name = 'Last name test'
    nickname = 'Nickname test'
    birthdate = '11.01.1999'
    city = 'New York'

    '''Выбираем используемый для тестов браузер. Устаналивается в variables'''
    def set_browser(self):
        browser = var.browser
        if browser == 'chrome':
            driver = webdriver.Chrome()
        if browser == 'firefox':
            driver = webdriver.Firefox()
        return driver

    def find_field(self, driver, name):
        location = ''
        fields = dict(first_name="first_name",
                      last_name="last_name",
                      nickname="nickname",
                      gender="label[for='genderMale']",
                      birthdate="birthdate",
                      city="input[data-vv-as='Город']")
        for field in fields.keys():
            if field == name:
                location = fields[field]
                break
            else:
                BaseException('ERROR')
        if name == 'gender' or name =='city':
            return driver.find_element_by_css_selector(location)
        else:
            return driver.find_element_by_id(location)


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
            first_name_el = self.find_field(browser, 'first_name')
            first_name_el.clear()
            first_name_el.send_keys(self.first_name)
            last_name_el = self.find_field(browser, 'last_name')
            last_name_el.clear()
            last_name_el.send_keys(self.last_name)
            nickname_el = self.find_field(browser,'nickname')
            nickname_el.clear()
            nickname_el.send_keys(self.nickname)
            gender_el = self.find_field(browser,'gender')
            gender_el.click()
            birthdate_el = self.find_field(browser,'birthdate')
            birthdate_el.clear()
            birthdate_el.send_keys(self.birthdate)
            city_el = self.find_field(browser,'city')
            city_el.send_keys(Keys.CONTROL + 'a')
            time.sleep(3)
            city_el.send_keys(Keys.DELETE)
            city_el.send_keys(self.city)
            save = browser.find_element_by_css_selector("button[type='submit']")
            #save.click()
            time.sleep(3)
        except Exception:
            browser.close()
            assert 1 == 2
