import json 
with open('test.json','r') as f:
	data_test = json.load(f)

def delete_conf_email():
	conf_emails = data_test['emails']
	for email in conf_emails:
		print(email['email'])

def delete_unconf_email():
	conf_emails = data_test['emails']
	for email in conf_emails:
		print(email['email'])



get_conf_email()