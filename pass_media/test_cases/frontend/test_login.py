from frontend.functions.authorization import Authorization
from selenium.webdriver.support.ui import WebDriverWait
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from selenium import webdriver
import variables as var
import time


class Test:

    domain = var.options[var.stand_for_test]
    cas_service = var.options['cas']
    oauth_service = var.options['oauth_pub']
    phone = var.options['phone']
    auth = Authorization()
    acc = Accounts()

    '''Выбираем используемый для тестов браузер. Устаналивается в variables'''
    def set_browser(self):
        browser = var.browser
        if browser == 'chrome':
            driver = webdriver.Chrome()
            WebDriverWait(driver, 2000)
        if browser == 'firefox':
            driver = webdriver.Firefox()
            WebDriverWait(driver, 500)
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

    '''Проверка доступности кнопки Далее при вводе валидного номера'''
    def test_enter_phone(self):
        browser = self.set_browser()
        try:
            browser.get(self.domain + '/cas/login/')
            browser.implicitly_wait(5)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" in status_btn, "button is dasabled!"
            enter = browser.find_element_by_class_name('phone__number').send_keys(self.phone)
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
        pwd = var.options['password']
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
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
            self.auth.set_phone(browser, self.phone)
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            password.submit()
            error = browser.find_element_by_class_name('form-message.form-message--error')
            assert error.text == 'Неверный пароль'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Отображение страницы регистрации при вводе незареганного номера'''
    def test_show_registration_page(self):
        browser = self.set_browser()
        phone = '+79990000000'
        lbl = 0
        try:
            self.auth.set_phone(browser, phone)
            title = browser.find_element_by_tag_name('h2')
            browser.implicitly_wait(3)
            assert '/accounts/register/' in browser.current_url
            assert title.text == 'Регистрация'
            phone_num = browser.find_element_by_css_selector("input[type='hidden']")
            assert phone_num.get_attribute('value') == phone
            info = browser.find_element_by_class_name('form-message.info')
            assert info.text == 'Проверьте номер телефона, на него будет отправлен код подтверждения'
            checkboxes = browser.find_elements_by_css_selector("input[type='checkbox']")
            for checkbox in checkboxes:
                assert not checkbox.is_selected(), "checkbox is selected"
            labels = browser.find_elements_by_class_name('checkbox__label')
            for label in labels:
                if 'Даю согласие на получение новостных, информационных рассылок' in label.text:
                    lbl += 1
                elif 'Даю согласие на обработку своих персональных данных согласно' in label.text:
                    lbl += 1
            assert lbl == 2, "не указаны оба пункта регистрации"
            next = browser.find_element_by_css_selector("button[type=submit]")
            assert 'is-disabled' in next.get_attribute('class'), "Кнопка далее доступна для нажатия"
        except Exception:
            browser.close()
            assert 1 == 2

    def test_authorization_cas_service(self):
        browser = self.set_browser()
        try:
            #Дозаполняем обязательные поля
            response = self.acc.get_account_info(self.cas_service).json()
            requireds = response['required_fields']
            need_update = []
            #проверяем есть ли незаполненные обязательные
            for required in requireds:
                have = response[required]
                if have == '' or have == []:
                    need_update.append(required)
            data = self.acc.generate_account_data(need_update)
            if data == {}:
                pass
            else:
                update = self.acc.update_account_info(data)
                assert update.status_code == 200, "не удалось обновить данные пользователя"
            self.auth.set_phone(browser, self.phone, self.cas_service)
            password = browser.find_element_by_name('password')
            password.send_keys(var.options['password'])
            password.submit()
            while self.cas_service+'/?ticket=ST-' not in browser.current_url:
                time.sleep(0.5)
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2


    '''Отображение пароля при нажатии на глазик'''
    def test_show_pwd(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            eye = browser.find_element_by_class_name('eye')
            eye.click()
            assert password.get_attribute('value') == 'qwerty12'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Смена номера по клику при вводе пароля'''
    def test_change_phone(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
            phone = browser.find_element_by_class_name('container-phone')
            phone.click()
            welcome = browser.find_element_by_css_selector('.form-title h2')
            assert welcome.text == 'Добро пожаловать!'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Кнопка Войти недоступна при пустом инпуте'''
    def test_disable_button(self):
        browser = self.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
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
            self.auth.set_phone(browser, self.phone)
            time.sleep(1)
            links = browser.find_elements_by_css_selector('button.link')
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = link
                    break
            otp.click()
            message = browser.find_element_by_class_name('form-message')
            assert message.text == msg
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''Повторная отправка ОТР'''
    def test_retry_send_otp(self):
        browser = self.set_browser()
        msg = 'Одноразовый код для входа был отправлен на ваш номер.'
        timer_text = 'Повторно код можно получить через '
        try:
            self.auth.set_phone(browser, self.phone)
            time.sleep(1)
            links = browser.find_elements_by_css_selector('button.link')
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = link
                    break
            otp.click()
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



    '''
    #Очистка таймера при смене номера, на который уже отправили код
    def test_success_login_by_otp(self):
        browser = self.set_browser()
        timer_text = 'Повторно код можно получить через'
        try:
            self.auth.set_phone(browser, self.phone)
            time.sleep(1)
            links = browser.find_elements_by_css_selector('button.link')
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = link
                    break
            otp.click()
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            phone = browser.find_element_by_class_name('container-phone')
            phone.click()
            self.auth.set_phone(browser, '+79999999999')
            next_button = browser.find_element_by_css_selector('.form-controls button')
            next_button.click()
            links = browser.find_elements_by_css_selector('button.link')
            otp = False
            for link in links:
                if link.text == 'Войти по одноразовому коду':
                    otp = True
                    break
            assert otp
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    #Авторизация с добавлением кук
    def test_cookie(self):
        browser = self.set_browser()
        try:
            self.auth.set_cookie(browser)
            assert '/accounts/edit' in browser.current_url
            personal = browser.find_element_by_class_name('form-title')
            assert personal.text == 'Личные данные'
        except Exception:
            browser.close()
            assert 1 == 2
    '''