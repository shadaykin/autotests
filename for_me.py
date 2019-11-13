import requests

session = requests.Session()
session.cookies.update({'sessionid':'l36y6z1jc2vk6fyvi1qnedb1e8ou53m2'})

response1 = session.get('https://pass.media/api/emails/')
response2 = session.get('https://pass.media/api/accounts/edit')

def req(session):
	s=session
	mr = s.get('https://pass.media/api/emails/')
	print(mr.text)
req(session)