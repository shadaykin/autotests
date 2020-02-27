import requests
import variables as var


class Sessions:

	def get_sessionid(self, env,*agrs):

		link = var.options[env] + '/cas/login'
		s = requests.Session()
		get_csrf = s.get(link)
		csrftoken = get_csrf.cookies['csrftoken']
		cookies = {'csrftoken': csrftoken}
		headers = {'X-CSRFToken': csrftoken, 'Referer': link}
		form_data = {'username': (None, var.options['phone']), 'password': (None, var.options['password'])}
		response = s.post(link, files=form_data, headers=headers, cookies=cookies)
		if len(agrs) == 0:
			session_id = {'sessionid': s.cookies['sessionid']}
		else:
			session_id = {'name': 'sessionid', 'value': s.cookies['sessionid']}
		return session_id
