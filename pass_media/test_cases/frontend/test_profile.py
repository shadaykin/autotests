from frontend.functions.authorization import Authorization
from backend.functions.emails import Emails
from backend.functions.cookies import Sessions
from backend.functions.accounts import Accounts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import variables as var
import time, pytest


@pytest.mark.usefixtures('delete_user','full_registration_account')
class TestProfile:
    domain = var.options[var.stand_for_test]
    auth = Authorization()
    acc = Accounts()
    eml = Emails()

    first_name = 'Name test'
    last_name = 'Last name test'
    nickname = 'Nickname test'
    birthdate = '11.01.1999'
    city = 'New York'

    def find_field(self, driver, name):
        """Поиск полей при редактировании"""
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
        if name == 'gender' or name == 'city':
            return driver.find_element_by_css_selector(location)
        else:
            return driver.find_element_by_id(location)

    def test_epmty_data(self):
        """Отображение уведомления о пустых данных"""
        message = 'Укажите, пожалуйста, информацию о себе, чтобы использовать её при регистрации через Pass.Media.'
        self.acc.update_all_account_info('empty')
        browser = self.auth.set_browser()
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            msg = browser.find_element_by_class_name('profile-form-message--border')
            assert message in msg.text
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_delete_account(self):
        """Удаление аккаунта в ЛК"""
        browser = self.auth.set_browser()
        dlt = ''
        cancel = ''
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            browser.find_element_by_link_text('Удалить аккаунт').click()
            """Страница ввода пароля"""
            title = browser.find_element_by_css_selector('.form-title > h2').text
            assert title == 'Удаление аккаунта'
            warning = browser.find_element_by_class_name('info-panel__title').text
            assert warning == 'Прочтите, это важно'
            content = browser.find_element_by_class_name('info-panel__content').text
            assert content == 'Ваш аккаунт будет удалён, и вы потеряете доступ к сервисам,' \
                              ' в которых были авторизованы с Pass.Media, ' \
                              'вместе со всеми данными.'
            delete = browser.find_element_by_css_selector('.app-button--ghost')
            assert 'is-disabled' in delete.get_attribute('class')
            browser.find_element_by_name('password').send_keys(var.options['password'])
            delete = browser.find_element_by_css_selector('.app-button--outlined')
            assert 'is-disabled' not in delete.get_attribute('class')
            delete.click()
            browser.find_element_by_class_name('textarea-input').send_keys('reason')
            buttons = browser.find_elements_by_tag_name('button')
            for button in buttons:
                if button.text == 'Удалить':
                    dlt = button
                elif button.text == 'Отменить':
                    cancel = button
            dlt.click()
            a = False
            b = 0
            while not a and b < 5:
                try:
                    assert browser.current_url == self.domain + '/cas/login/', "can't redirect to welcome"
                    a = True
                except:
                    time.sleep(0.5)
                    b += 1
            assert a
            browser.close()
        except:
            browser.close()
            assert 1 == 2


    def test_data_edit(self):
        """Проверка заполнения личных данных в ЛК"""
        browser = self.auth.set_browser()
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            personal = browser.find_element_by_tag_name('h2')
            assert personal.text == 'Личные данные'
            edit = browser.find_element_by_class_name('link__icon.icon.icon-edit')
            edit.click()
            first_name_el = self.find_field(browser, 'first_name')
            first_name_el.send_keys(self.first_name)
            last_name_el = self.find_field(browser, 'last_name')
            last_name_el.send_keys(self.last_name)
            nickname_el = self.find_field(browser, 'nickname')
            nickname_el.send_keys(self.nickname)
            gender_el = self.find_field(browser, 'gender')
            birthdate_el = self.find_field(browser, 'birthdate')
            birthdate_el.click()
            birthdate_el.send_keys(self.birthdate)
            city_el = self.find_field(browser, 'city')
            city_el.send_keys(self.city)
            save = browser.find_element_by_css_selector("button[type='submit']")
            save.click()
            time.sleep(2)
            profiles = browser.find_elements_by_css_selector(".user-info-wrapper div")
            a = 0
            for profile in profiles:
                if profile.text == self.first_name:
                    a += 1
                elif profile.text == self.last_name:
                    a += 1
                elif profile.text == self.nickname:
                    a += 1
            assert a == 3
            bd = browser.find_element_by_class_name('profile-info-item--birthdate')
            assert bd.text == self.birthdate
            city = browser.find_element_by_class_name('profile-info-item--city')
            assert city.text == self.city
            browser.close()
        except Exception:
            browser.close()
            assert 1 == 2

    def test_email_prfoile(self):
        """Блок email"""
        browser = self.auth.set_browser()
        email_title = False
        dcrpn = 'Используется для восстановления доступа к аккаунту и авторизации в ваших сервисах.'
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            titles = browser.find_elements_by_tag_name('h3')
            for title in titles:
                if title.text == 'Электронная почта':
                    email_title = True
                    break
            assert email_title, 'Don`t have email title'
            description = browser.find_element_by_class_name('profile-form-message--email')
            assert description.text == dcrpn
            add = browser.find_element_by_class_name('add-email')
            assert add.text == 'Добавить адрес'
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_add_unconf_email(self):
        """Добавление неподтвержденного адреса"""
        browser = self.auth.set_browser()
        try:
            email = var.options['email']
            add_btn = ''
            unc_list = self.eml.emails_unconfirmed_list()
            conf_list = self.eml.emails_confirmed_list()
            if len(unc_list) != 0:
                self.eml.emails_delete_unconfirmed()
            if len(conf_list) != 0:
                self.eml.emails_delete_confirmed()
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            add = browser.find_element_by_css_selector('.add-email .link.link--icon')
            # Прокручиваем страницу до элемента "добавить адрес"
            browser.execute_script('arguments[0].scrollIntoView(true);', add)
            browser.execute_script("arguments[0].click();", add)
            # Создаем объекты кнопок
            buttons = browser.find_elements_by_tag_name('button')
            for button in buttons:
                if button.text == 'Добавить':
                    add_btn = button
            time.sleep(1)
            # Находим инпут email и вводим адрес
            add_email = browser.find_element_by_id('email')
            browser.execute_script('arguments[0].scrollIntoView(true);', add_email)
            add_email.send_keys(email)
            # Добавляем введенный адрес
            add_btn.click()
            browser.execute_script('arguments[0].scrollIntoView(true);', add_btn)
            browser.execute_script("arguments[0].click();", add_btn)
            time.sleep(2)
            # Провереяем выполнение условий кейса
            description = browser.find_element_by_class_name('confirm-email__inside .profile-form-message')
            assert "Адрес не подтвержден" in browser.find_element_by_css_selector('.list__item-content .form-message.error').text
            assert "Код отправлен на %s. Введите код в поле ниже или перейдите " \
                   "по ссылке из письма, затем нажмите «Подтвердить»." % email in description.text
            assert "Повторно код можно получить через" in browser.find_element_by_class_name('confirm-email__resend .form-message').text
            assert browser.find_element_by_name('confirmation_key')
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_add_incorrect_email(self):
        """Добавляем некорректный email"""
        browser = self.auth.set_browser()
        add_btn = ''
        cancel_btn = ''
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            add = browser.find_element_by_css_selector('.add-email .link.link--icon')
            browser.execute_script('arguments[0].scrollIntoView(true);', add)
            browser.execute_script("arguments[0].click();", add)
            buttons = browser.find_elements_by_tag_name('button')
            for button in buttons:
                if button.text == 'Добавить':
                    add_btn = button
            time.sleep(1)
            add_email = browser.find_element_by_id('email')
            browser.execute_script('arguments[0].scrollIntoView(true);', add_email)
            add_email.send_keys('test.mail.ru')
            assert add_email.get_attribute('aria-invalid')
            assert "Неверный адрес" in browser.find_element_by_css_selector('.form-input .form-message--error').text
            assert 'is-disabled' in add_btn.get_attribute('class')
            time.sleep(2)
            browser.close()
        except:
            browser.close()
            assert 1 == 2

    def test_logout_profile(self):
        """Выход из личного кабинета"""
        browser = self.auth.set_browser()
        yes_btn = ''
        no_btn = ''
        try:
            self.auth.set_cookie(browser)
            assert browser.current_url == self.domain + '/accounts/edit'
            exit = browser.find_element_by_css_selector('.icon-exit')
            browser.execute_script('arguments[0].scrollIntoView(true);', exit)
            browser.execute_script("arguments[0].click();", exit)
            buttons = browser.find_elements_by_tag_name('button')
            for button in buttons:
                if button.text == 'Нет':
                    no_btn = button
            no_btn.click()
            assert '/accounts/edit' in browser.current_url
            exit = browser.find_element_by_css_selector('.icon-exit')
            browser.execute_script('arguments[0].scrollIntoView(true);', exit)
            browser.execute_script("arguments[0].click();", exit)
            time.sleep(1)
            buttons = browser.find_elements_by_tag_name('button')
            for button in buttons:
                if button.text == 'Да':
                    yes_btn = button
            yes_btn.click()
            assert '/cas/login' in browser.current_url
            browser.close()
        except:
            browser.close()
            assert 1 == 2
