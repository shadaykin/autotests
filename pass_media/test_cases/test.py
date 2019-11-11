from functions.params import Emails
from enviroments import options as o
env = 'prod'

obj = Emails()

#delete = obj.delete_unconfirmed_email(env)

#add = obj.add_email(env)

email = obj.emails_unconfirmed_list(env)

em = [o['email']]
print(em)
if email == em: 	
	print('success')
else:
	print('no')
print(email)