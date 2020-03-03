from frontend.functions.authorization import Authorization
from backend.functions.cookies import Sessions
from selenium import webdriver
import variables as var
import time


class Test:

    domain = var.options[var.stand_for_test]
    auth = Authorization()

    '''Выбираем используемый для тестов браузер. Устаналивается в variables'''
    def set_browser(self):
        browser = var.browser
        if browser == 'chrome':
            driver = webdriver.Chrome()
        if browser == 'firefox':
            driver = webdriver.Firefox()
        return driver

    '''Проверка приветственной страницы, без валидного
        номера кнопка "Далее" не активна'''
    def test_welcome(self):
        browser = self.set_browser()
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

    '''Ввод валидного номера телефона'''
    def test_enter_phone(self):
        phone = var.options['phone'][2:12]
        browser = self.set_browser()
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(2)
            enter = self.auth.enter_phone_number(browser, phone)
            time.sleep(1)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" not in status_btn, "button is dasabled!"
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Ввод корректного пароля'''
    def test_enter_correct_pwd(self):
        phone = var.options['phone'][2:12]
        pwd = var.options['password']
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            password = browser.find_element_by_name('password')
            password.send_keys(pwd)
            password.submit()
            time.sleep(1)
            assert browser.current_url == self.domain + '/accounts/edit'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Ввод некорректного пароля'''
    def test_enter_incorrect_pwd(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            password.submit()
            time.sleep(1)
            error = browser.find_element_by_class_name('form-message.form-message--error')
            assert error.text == 'Неверный пароль'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Отображение пароля при нажатии на глазик'''
    def test_show_pwd(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            eye = browser.find_element_by_class_name('eye')
            eye.click()
            assert password.get_attribute('value') == 'qwerty12'
            time.sleep(1)
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Смена номера по клику при вводе пароля'''
    def test_change_phone(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            phone = browser.find_element_by_class_name('container-phone')
            phone.click()
            welcome = browser.find_element_by_css_selector('.form-title h2')
            assert welcome.text == 'Добро пожаловать!'
            time.sleep(1)
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Кнопка Войти недоступна при пустом инпуте'''
    def test_disable_button(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            enter = browser.find_element_by_css_selector('.form-controls button')
            status_enter = enter.get_attribute('class')
            assert "is-disabled" in status_enter, "button is dasabled!"
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            enter = browser.find_element_by_css_selector('.form-controls button')
            status_enter = enter.get_attribute('class')
            assert "is-disabled" not in status_enter, "button is dasabled!"
            time.sleep(1)
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Успешная отправка одноразового пароля'''
    def test_success_login_by_otp(self):
        browser = self.set_browser()
        msg = 'Одноразовый код для входа был отправлен на ваш номер.'
        timer_text = 'Повторно код можно получить через'
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            links = browser.find_elements_by_css_selector('button.link')
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = link
                    break
            otp.click()
            time.sleep(1)
            message = browser.find_element_by_class_name('form-message')
            assert message.text == msg
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_retry_send_otp(self):
        browser = self.set_browser()
        msg = 'Одноразовый код для входа был отправлен на ваш номер.'
        timer_text = 'Повторно код можно получить через '
        try:
            self.auth.set_phone(browser)
            time.sleep(1)
            links = browser.find_elements_by_css_selector('button.link')
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = link
                    break
            otp.click()
            time.sleep(1)
            message = browser.find_element_by_class_name('form-message')
            assert message.text == msg
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            time.sleep(60)
            retry = browser.find_element_by_css_selector('button.link')
            assert retry.text == 'Получить код повторно'
            retry.click()
            time.sleep(2)
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2