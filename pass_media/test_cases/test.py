from functions.params import Emails
from enviroments import options as o


obj = Emails()

a = obj.emails_unconfirmed_list()

if len(a) == 0:
	print('0')
else:
	print('HAVE')

