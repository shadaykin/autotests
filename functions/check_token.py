import requests
from selenium import webdriver
import time, json

def check_token(client_id,redirect_uri,browser):
	url = 'https://passport.jw-test.zxz.su/'
	add_url = ('oauth/authorize?','oauth/token/','oauth/resource/profile/')
	payload = (('response_type','code'),('client_id',client_id),('redirect_uri',redirect_uri))
	browser.get(url+add_url[0]+'response_type=code&client_id='+client_id+'&redirect_uri='+redirect_uri)
	time.sleep(1)
	
	access = browser.find_element_by_class_name("btn")
	access.submit()
	time.sleep(3)
	
	try:
		code = browser.current_url.split("code=")[1]
	except:
		print('Access denied')
	
	
	browser.quit()
	
	payload = {'grant_type':'authorization_code','code':code,'client_id':client_id,'redirect_uri':redirect_uri}
	get_token = requests.post(url+add_url[1],data = payload)
	
	access_token = json.loads(get_token.text)
	headers = {'Authorization': 'Bearer '+access_token["access_token"]}
	check_token = requests.get(url+add_url[2],headers = headers)
	assert check_token.status_code == 200
	
	
	