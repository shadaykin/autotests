from selenium import webdriver
from functions.clear_cash import Cookie
from functions.authorization import Authorization

service = 'https://yandex.ru'

def test_auth_cas():
    cash = Cookie.clear_cash_func()
    driver = webdriver.Firefox(cash)
    client_id = 'OH9tXjoxx0gmucjCJYXTdKQKWIdXpMksMZ2IKtEg'
    redirect_uri = 'http://localhost/'

    # driver.maximize_window()
    try:
        Authorization.correct_auth_oauth(driver, client_id, redirect_uri)
    except:
        assert 1 == 2, driver.close()


