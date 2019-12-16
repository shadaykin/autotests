import requests, json, time
import variables as var
import data_request as dr
from functions.cookies import Sessions

class Services:

    env = var.stand_for_test

    cookie = Sessions().get_sessionid(env)
    session = requests.Session()
    session.cookies.update(cookie)
    link = var.options[env]
    endpoint = var.endpoints_account
    url = link + '/oauth/authorize/?response_type=code&redirect_uri=https://localhost111&'

    def get_auth_code(self, *args):
        """Получение кода авторизация"""
        post = self.session.post(url+var.options['oauth_pub'])
