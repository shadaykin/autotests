import requests, json, time
import variables as var
from selenium import webdriver
from backend.functions.cookies import Sessions


env = var.stand_for_test


browser = webdriver.Chrome()


def set_cookie(browser):
    try:
        browser.get(self.domain + '/cas/login/')
        cookie = Sessions().get_sessionid(var.stand_for_test, 1)
        browser.add_cookie(cookie)
        browser.refresh()
        edit = False
        n = 0
        while not edit and n < 5:
            try:
                assert '/accounts/edit' in browser.current_url
                edit = True
            except:
                time.sleep(0.5)
                n += 1
        assert edit
    except:
        print("Can`t add cookie")
        browser.close()
        assert 1 == 2

set_cookie(browser)


