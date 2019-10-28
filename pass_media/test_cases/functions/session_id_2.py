import requests
import enviroments
import sys


def get_sessionid(env):

    link = enviroments.options['prod']
    s = requests.Session()
    get_csrf = s.get(link)
    csrftoken = get_csrf.cookies['csrftoken']
    cookies = {'csrftoken': csrftoken}
    headers = {
        'X-CSRFToken': csrftoken, 'Referer': link
    }
    files = {'username': (None, enviroments.options['phone']), 'password': (None, enviroments.options['password'])}
    response = s.post(link, files=files, headers=headers, cookies=cookies)
    session_id = {'sessionid': s.cookies['sessionid']}
    return session_id

print(get_sessionid('prod'))









