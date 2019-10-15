import requests
import enviroments
def get_sessionid():
    link = "https://passport.jw-test.zxz.su/cas/login"
    req = requests.get(link)
    csrftoken=req.cookies['csrftoken']
    payload = {'username': enviroments.options['phone'], 'password': enviroments.options['password']}




get_sessionid()