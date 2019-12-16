import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import data_response as d_res
import variables as var
from functions.cookies import Sessions
from selenium import webdriver
from functions.emails import Emails
from functions.accounts import Accounts

browser = webdriver.Chrome()

env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)

cookies = {'sessionid':'1234234242'}
browser.add_cookie(cookies)
browser.get('https://passport.jw-test.zxz.su/accounts/edit')