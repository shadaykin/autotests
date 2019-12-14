import requests, json
from datetime import datetime, timedelta
import data_request as dr
import data_response as dr
import variables as var
from functions.cookies import Sessions
from functions.emails import Emails
from functions.accounts import Accounts

'''
env = var.stand_for_test

cookie = Sessions().get_sessionid(env)
session = requests.Session()
session.cookies.update(cookie)
'''

put = Accounts().put_account_education('special_ed')
ed = Accounts().get_account_education().json()
print(ed)
'''
ed_inst = ed['institutions'][0]

higher_ed =	{
	"level":"higher",
	"institutions":[
		{"id":20327,"year":2020,"speciality":"спец",
		"country":{"id":2,"title":"Россия","code":"RU"},
		"city":{"id":375,"country":2,"title":"Москва","area":None,"region":None},
		"degree":"Бакалавр","education":20259,
		"university":{"id":602,"title":"НИУ МЭИ","country":2,"city":375}}
	]}
	
higher_inst = higher_ed['institutions'][0]
#print(higher_inst)

assert ed['level'] == higher_ed['level']
for key in ed_inst.keys():
	if key == 'education' or key == 'id':
		pass
	else:
		assert higher_inst[key] == ed_inst[key]

'''
#assert dt.higher_ed in resp
#print(resp['institutions'][0]['education'])
#print(resp['institutions'][0]['id'])
		