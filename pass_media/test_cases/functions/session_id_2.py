import requests

def get_sessionid():
    link = "https://passport.jw-test.zxz.su/cas/login"

    s = requests.Session()
    get_csrf = s.get(link)
    csrftoken = get_csrf.cookies['csrftoken']
    cookies = {'csrftoken': csrftoken}
    headers = {
        'X-CSRFToken': csrftoken, 'Referer': link
    }
    files = {'username': (None, '+79096201687'), 'password': (None, '111111xX')}

    response = s.post(link, files=files, headers=headers, cookies=cookies)

    print(s.cookies.get_dict())



get_sessionid()