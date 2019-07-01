from selenium import webdriver
from functions.clear_cash import Cookie
from functions.authorization import Authorization

service = 'https://tnt-club.com'

def test_auth_cas():
    cash = Cookie.clear_cash_func()
    driver = webdriver.Firefox(cash)

    # driver.maximize_window()
    try:
        Authorization.correct_auth_cas(driver,service)
        redirect_uri = driver.current_url.split('https://')[1]
        print(redirect_uri)
        driver.close()
    except:
        assert 1 == 2, driver.close()

test_auth_cas()


