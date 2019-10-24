def emails():
	from functions import session_id_2 as sid2
	qq=sid2.get_sessionid(prod)
	print(qq)

emails()
