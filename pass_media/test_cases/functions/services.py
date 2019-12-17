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

    def get_pmid(self):
        """Получение pass.media_id"""
        url = self.link + var.endpoints_service['pmid']
        pmid = self.session.get(url)
        return pmid.json()['id']

    def get_service_info(self, service):
        """Получение данных по сервису"""
        url = self.link + var.endpoints_service['service_info']
        info = self.session.get(url+service)
        return info

    def get_api_key(self, pmid):
        """Получение передаваемых полей по api-key"""
        url = self.link+var.endpoints_service['api_key']
        if self.env == 'prod':
            headers = {'api-key': '96618d5e24e19e760600296fb3d9dad1f529e08caa8c18f17c1a3b0f410a48cb'}
        else:
            headers = {'api-key': 'c41350d8e80f15e2dca47fc5637cf208ac9b015feecdcdff8ea319f68ed89a51'}
        api_key = self.session.get(url+pmid, headers=headers)
        return api_key

    def get_auth_code(self, *args):
        """Получение кода авторизация"""
        pass
