import requests, json, time
from datetime import datetime, timedelta
import data_request as dr
import response_service as resp_acc
import variables as var
#from functions.cookies import Sessions
from selenium import webdriver
from functions.emails import Emails
from functions.accounts import Accounts
from functions.services import Services

'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)
'''

data = {"results": [
		{
			"city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
			"full_name": "г Москва"
		},
		{
			"city_guid": "4ae6d306-349e-4fb8-9ce9-7c3735d3c4e6",
			"full_name": "г Мосальск, р-н Мосальский, обл Калужская"
		}]}

print(data["results"][1]["full_name"])