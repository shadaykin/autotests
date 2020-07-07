from frontend.functions.authorization import Authorization
from selenium.webdriver.support.ui import WebDriverWait
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from selenium import webdriver
import variables as var
import time, pytest

@pytest.mark.usefixtures('disable_recaptcha')
class Test:

    domain = var.options[var.stand_for_test]
    cas_service = var.options['cas']
    oauth_service = var.options['oauth_pub']
    phone = var.options['phone']
    auth = Authorization()
    acc = Accounts()

    def test_welcome(self):
        """Проверка приветственной страницы, без валидного
                номера кнопка "Далее" не активна"""
        browser = self.auth.set_browser()
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(2)
            assert browser.title == 'Pass.Media – единый аккаунт для вселенной развлекательных сервисов'
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" in status_btn
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_enter_phone(self):
        """Проверка доступности кнопки Далее при вводе валидного номера"""
        browser = self.auth.set_browser()
        try:
            browser.get(self.domain + '/cas/login/')
            time.sleep(2)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" in status_btn, "button is not disabled!"
            browser.find_element_by_class_name('phone__number').send_keys(self.phone[2:12])
            time.sleep(1)
            next_button = browser.find_element_by_css_selector('.form-controls button')
            status_btn = next_button.get_attribute('class')
            assert "is-disabled" not in status_btn, "button is disabled!"
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_enter_correct_pwd(self):
        """Ввод корректного пароля"""
        pwd = var.options['password']
        browser = self.auth.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
            password = browser.find_element_by_name('password')
            password.send_keys(pwd)
            password.submit()
            time.sleep(2)
            assert browser.current_url == self.domain + '/accounts/edit'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_enter_incorrect_pwd(self):
        """Ввод некорректного пароля"""
        browser = self.auth.set_browser()
        try:
            self.auth.set_phone(browser, self.phone)
            password = browser.find_element_by_name('password')
            password.send_keys('qwerty12')
            password.submit()
            browser.implicitly_wait(5)
            error = browser.find_element_by_class_name('form-message.form-message--error')
            assert error.text == 'Неверный пароль'
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_show_registration_page(self):
        """Отображение страницы регистрации при вводе незареганного номера"""
        browser = self.auth.set_browser()
        phone = '+80012387654'
        lbl = 0
        try:
            self.auth.set_phone(browser, phone, 'test')
            title = browser.find_element_by_tag_name('h2')
            browser.implicitly_wait(3)
            assert title.text == 'Регистрация'
            phone_num = browser.find_element_by_css_selector("input[type='hidden']")
            assert phone_num.get_attribute('value') == phone
            checkboxes = browser.find_elements_by_css_selector("input[type='checkbox']")
            for checkbox in checkboxes:
                assert not checkbox.is_selected(), "checkbox is selected"
            labels = browser.find_elements_by_class_name('checkbox__label')
            for label in labels:
                if 'Даю согласие на получение новостных, информационных рассылок' in label.text:
                    lbl += 1
                elif 'Даю согласие на обработку своих персональных данных согласно' in label.text:
                    lbl += 1
            assert lbl == 2, "не отображены оба пункта регистрации"
            next = browser.find_element_by_css_selector("button[type=submit]")
            assert 'is-disabled' in next.get_attribute('class'), "Кнопка далее доступна для нажатия"
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_authorization_cas_service(self):
        """Авторизация в CAS-сервисе"""
        browser = self.auth.set_browser()
        cookie = Sessions().get_sessionid(var.stand_for_test)
        self.acc.session.cookies.update(cookie)
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

    def test_show_pwd(self):
        """Отображение пароля при нажатии на глазик"""
        browser = self.auth.set_browser()
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

    def test_change_phone(self):
        '''Смена номера по клику при вводе пароля'''
        browser = self.auth.set_browser()
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

    def test_disable_button(self):
        browser = self.auth.set_browser()
        """Кнопка Войти недоступна при пустом инпуте"""
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

    def test_success_send_otp(self):
        """Успешная отправка одноразового пароля"""
        browser = self.auth.set_browser()
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
            browser.implicitly_wait(5)
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_retry_send_otp(self):
        """Повторная отправка ОТР"""
        browser = self.auth.set_browser()
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
            browser.implicitly_wait(5)
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            time.sleep(60)
            retry = browser.find_element_by_css_selector('button.link')
            assert retry.text == 'Получить код повторно'
            retry.click()
            browser.implicitly_wait(5)
            timer = browser.find_element_by_class_name('form-message.form-message--color')
            assert timer_text in timer.text
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    '''
    def test_success_login_by_otp(self):
        #Очистка таймера при смене номера, на который уже отправили код
        browser = self.auth.set_browser()
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

    '''