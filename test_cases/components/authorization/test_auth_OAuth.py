from selenium import webdriver
from functions.clear_cash import Cookie
from functions.authorization import Authorization


def test_auth_oauth():
    cash = Cookie.clear_cash_func()
    driver = webdriver.Firefox(cash)
    client_id = 'OH9tXjoxx0gmucjCJYXTdKQKWIdXpMksMZ2IKtEg'
    redirect_uri = 'http://localhost/'

    # driver.maximize_window()
    try:
        Authorization.correct_auth_oauth(driver, client_id, redirect_uri)
        driver.close()
    except:
        assert 1 == 2, driver.close()


