import random
import time
import merch.variables as var
from merch.functions.order import Orders
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCases:
    order = Orders()
    gateway = var.gateway
    env = var.enviroment

    def test_permission_api(self):
        fail = []
        for endpoint in var.processing_endpoints:
            if endpoint == 'binding':
                pass
            else:
                make_request = requests.get(var.enviroments[self.env]+var.processing_endpoints[endpoint])
                if make_request.status_code != 403:
                    fail.append(endpoint)
        if len(fail) != 0:
            assert 1 == 2, print('API who available without functions: ' + str(fail))