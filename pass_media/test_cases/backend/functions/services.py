import requests, json, time
import variables as var
import backend.data_request as dr
from backend.functions.cookies import Sessions

class Services:

    env = var.stand_for_test

    cookie = Sessions().get_sessionid(env)
    session = requests.Session()
    session.cookies.update(cookie)
    link = var.options[env]
    endpoint = var.endpoints_account

    def get_pmid(self, session):
        """Получение pass.media_id"""
        url = self.link + var.endpoints_service['pmid']
        pmid = session.get(url)
        return pmid.json()['id']

    def get_service_info(self, service):
        """Получение данных по сервису"""
        url = self.link + var.endpoints_service['service_info']
        info = requests.get(url+service)
        return info

    def get_api_key(self, pmid):
        """Получение передаваемых полей по api-key"""
        url = self.link+var.endpoints_service['api_key']
        if self.env == 'prod':
            headers = {'api-key': var.options['api_key_prod']}
        else:
            headers = {'api-key': var.options['api_key']}
        api_key = self.session.get(url+pmid, headers=headers)
        return api_key

    def get_auth_code(self, *args):
        """Получение кода авторизация"""
        pass
