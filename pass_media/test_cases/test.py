from functions.params import Session
from functions.params import Emails
from enviroments import options as o


s = Session()

e = Emails()
incorrect = 'email@email'
#a = e.emails_delete_unconfirmed()

def test_remove_unconfirmed_email():
		unc_list = e.emails_unconfirmed_list()
		
		if len(unc_list) != 0:
			remove = e.emails_delete_unconfirmed()
			assert remove.status_code >= 200 and remove.status_code < 210
			unc_list
			assert len(unc_list) == 0
		else:
			e.emails_add()
			unc_list
			print(unc_list)
			remove = e.emails_delete_unconfirmed()
			assert remove.status_code >= 200 and remove.status_code < 210
			unc_list
			assert len(unc_list) == 0