import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import data_response as d_res
import variables as var
from functions.cookies import Sessions
from selenium import webdriver
from functions.emails import Emails
from functions.accounts import Accounts
from functions.services import Services


env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

service = 'https://localhost'
pmid = Services().get_pmid()
print(pmid)
api = Services().get_api_key(pmid)
print(api.text)