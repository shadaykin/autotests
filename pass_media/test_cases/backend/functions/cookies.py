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
		if 'register' in args:
			data = {"username": var.options['phone'], "password": var.options['password'],
					"tos": True, "accept_targeting": False}
		else:
			data = {"username": var.options['phone'], "password": var.options['password']}
		response = s.post(link, data=data, headers=headers, cookies=cookies)
		assert response.status_code == 200, "can't authorize"
		assert response.json()['authenticated']
		if len(args) == 0 or 'register' in args:
			session_id = {'pm_sid': s.cookies['pm_sid']}
			return session_id
		else:
			session_id = {'name': 'pm_sid', 'value': s.cookies['pm_sid']}
			return session_id