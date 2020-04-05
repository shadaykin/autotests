import requests
import variables as var


class Sessions:

	def get_sessionid(self, env, *args):
		link = var.options[env] + '/api/cas/login/'
		s = requests.Session()
		get_csrf = s.get(link)
		csrftoken = get_csrf.cookies['csrftoken']
		cookies = {'csrftoken': csrftoken}
		headers = {'X-CSRFToken': csrftoken, "Referer": var.options[env]}
		data = {"username": var.options['phone'], "password": var.options['password']}
		response = s.post(link, data=data, headers=headers, cookies=cookies)
		if len(args) == 0:
			session_id = {'sessionid': s.cookies['sessionid']}
		else:
			session_id = {'name': 'sessionid', 'value': s.cookies['sessionid']}
		return session_id