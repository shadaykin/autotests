import pytest
import time
import variables as var
from backend.functions.accounts import Accounts
from backend.functions.cookies import Sessions
from backend.functions.emails import Emails
from backend.functions.services import Services
from frontend.functions.authorization import Authorization
from selenium.webdriver.support.ui import Select

domain = var.options[var.stand_for_test]


@pytest.fixture(scope='class')
def delete_user():
    check = Accounts().check_phone()
    if check.json()['success']:
        try:
            browser = Authorization().set_browser()
            Authorization().auth_admin(browser)
            browser.get(browser.current_url + '/passport/user/?q=' + var.options['phone'])
            browser.refresh()
            browser.implicitly_wait(5)
            browser.find_element_by_css_selector('.row1 [type=checkbox]').click()
            select = Select(browser.find_element_by_name('action'))
            select.select_by_visible_text('Delete selected objects')
            go = browser.find_element_by_name('index')
            go.click()
            yes = browser.find_element_by_css_selector('[type=submit]')
            browser.execute_script('arguments[0].scrollIntoView(true);', yes)
            browser.execute_script("arguments[0].click();", yes)
            success = browser.find_element_by_class_name('success')
            assert 'Success' in success.text
            browser.close()
        except:
            browser.close()
            assert 1 == 2, "can't delete user"
    else:
        pass

@pytest.fixture(scope='class')
def disable_recaptcha():
    """Отключаем капчу"""
    try:
        browser = Authorization().set_browser()
        Authorization().auth_admin(browser)
        config = browser.find_element_by_link_text('Config')
        config_url = config.get_attribute('href')
        browser.get(config_url)
        time.sleep(1)
        select = Select(browser.find_element_by_name('DISABLE_RECAPTCHA'))
        select.select_by_visible_text('Да')
        browser.find_element_by_name('_save').click()
        browser.close()
    except:
        browser.close()
        assert 1 == 2, "can't disable reCaptcha"

@pytest.fixture(scope='class')
def full_registration_account(disable_recaptcha):
    """Полная регистрация пользователя"""
    check = Accounts().check_phone()
    if check.json()['success']:
        pass
    else:
        browser = Authorization().set_browser()
        reg = Accounts().register_account()
        assert reg.status_code == 201
        Authorization().auth_admin(browser)
        browser.get(browser.current_url + '/passport/user/?q=' + var.options['phone'])
        browser.refresh()
        browser.find_element_by_css_selector('.row1 .field-pk').click()
        time.sleep(1)
        title = browser.find_element_by_css_selector('#content>h1').text
        assert title == 'Change user'
        browser.find_element_by_partial_link_text('this form').click()
        pwd1 = browser.find_element_by_name('password1')
        pwd1.send_keys(var.options['password'])
        pwd2 = browser.find_element_by_name('password2')
        pwd2.send_keys(var.options['password'])
        pwd2.submit()
        success = browser.find_element_by_class_name('success')
        assert 'success' in success.text
        #browser.find_element_by_name('is_confirmed').click()
        #save = browser.find_elements_by_name('_addanother')
        #save.click()
        #assert 'successfully' in browser.find_element_by_class_name('success')
        browser.close()
        finish = Sessions().get_sessionid(var.stand_for_test, 'register')
        Emails().session.cookies.update(finish)
        Accounts().session.cookies.update(finish)
        Services().session.cookies.update(finish)


@pytest.fixture()
def update_session(session):
    cookie = Sessions().get_sessionid(var.stand_for_test)
    session.cookies.update(cookie)



def ff(full_registration_account):
    pass