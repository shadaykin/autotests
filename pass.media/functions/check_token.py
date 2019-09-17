import requests
from selenium import webdriver
import time, json

def check_token(client_id,redirect_uri,code):

	add_url = ('oauth/token/', 'oauth/resource/profile/')
	payload = {'grant_type':'authorization_code','code':code,'client_id':client_id,'redirect_uri':redirect_uri}
	get_token = requests.post(url+add_url[0], data=payload)
	
	access_token = json.loads(get_token.text)
	headers = {'Authorization': 'Bearer '+access_token["access_token"]}
	check_token = requests.get(url+add_url[1], headers=headers)
	assert check_token.status_code == 200
	
	
	