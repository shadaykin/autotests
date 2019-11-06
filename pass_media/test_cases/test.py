from functions.params import Emails

env = 'prod'
endpoint = 'email'

obj = Emails()
email_con = obj.emails_confirmed_list(env)
email_uncon = obj.emails_unconfirmed_list(env)

print(email_con)
print(email_uncon)
