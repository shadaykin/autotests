from functions.cookies import Sessions
from functions.emails import Emails

obj = Emails().emails_unconfirmed_list()

for email in obj:
	print(email)