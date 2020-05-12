import requests, json, time, datetime, pytest
import variables as var

from selenium import webdriver

'''
from backend.functions.cookies import Sessions
from backend.functions.emails import Emails
from backend.functions.accounts import Accounts
from selenium.webdriver.support.ui import Select
from frontend.functions.authorization import Authorization
'''


# env = var.stand_for_test
# acc = Accounts()
# service = var.options['cas']
# auth = Authorization()

@pytest.fixture(scope='class')
def success():
    browser = webdriver.Chrome()
    time.sleep(5)
    browser.close()


@pytest.mark.usefixtures('success')
class TestSomething:

    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 1 == 1
