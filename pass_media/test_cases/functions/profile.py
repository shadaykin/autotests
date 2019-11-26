import requests, json, time
import enviroments as e
from selenium import webdriver
from functions.cookies import Sessions

class Profiles:

	env = e.stand_for_test

	cookie = Sessions().get_sessionid(env)
	session = requests.Session()
	session.cookies.update(cookie)

	expect = '
	{"phone":"+79096201687",
	"first_name":"",
	"last_name":"",
	"nickname":"",
	"emails_confirmed":[],
	"emails_unconfirmed":["shadayka152+1@gmail.com","shadayka152+3@gmail.com","shadayka152+4@gmail.com","shadayka152+2@gmail.com"],
	"gender":"",
	"phone_country":"RU",
	"city":"",
	"city_guid":null,
	"birthdate":null,
	"age":null,
	"required_fields":[],
	"optional_fields":[],
	"required_empty_only":false}'