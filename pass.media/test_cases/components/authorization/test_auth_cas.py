from selenium import webdriver
from functions.clear_cash import Cookie
from functions.authorization import Authorization

service = 'https://yandex.ru'

def test_auth_cas():
    cash = Cookie.clear_cash_func()
    driver = webdriver.Firefox(cash)

    # driver.maximize_window()
    try:
        Authorization.correct_auth_cas(driver,service)
        redirect_uri = driver.current_url.split('https://')[1]
        check = 'yandex.ru/?ticket='
        if check in redirect_uri:
            driver.close()
        else:
            assert 1 == 2, driver.close()
    except:
        assert 1 == 2, driver.close()


