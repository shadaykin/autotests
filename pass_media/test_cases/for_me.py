import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import response_service as resp_acc
import variables as var
from functions.cookies import Sessions
from selenium import webdriver
from functions.emails import Emails
from functions.accounts import Accounts
from functions.services import Services


env = var.stand_for_test
'''
cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)
'''

service = var.options['oauth_pub']
info = Services().get_service_info(service)

print(info.text)
