from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, json, sys
from functions.clear_cash import Cookie
from functions.authorization import Authorization

service='https://yandex.ru'

def test_auth_success():
    cash = Cookie.clear_cash_func()
    driver = webdriver.Firefox(cash)

    # driver.maximize_window()
    try:
        Authorization.correct_auth_cas(driver,service)
        assert "accounts/complete == driver.current_url.split("https://passport.jw-test.zxz.su/")[1], driver.close()
        driver.close()
    except:
        assert 1 == 2, driver.close()


