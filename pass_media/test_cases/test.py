from functions.params import Emails

env = 'prod'
endpoint = 'email'

obj = Emails()

email_count = obj.emails_count(env)
print(email_count)

email_delete = obj.delete_unconfirmed_email(env)

email_count = obj.emails_count(env) 	
print(email_count)

