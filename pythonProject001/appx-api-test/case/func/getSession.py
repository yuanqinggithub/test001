import os
import sys
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.func.login import Login
from case.func.getUserToken import GetUserToken

def getSession(proxies=None):
    s = requests.session()
    l = Login(s)
    token,appid = l.getTokenAndAppID(proxies=proxies)
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    get_token = GetUserToken(s)
    real_token = get_token.getToken(appid=appid,proxies=proxies)
    h = {'Authorization':real_token}
    s.headers.update(h)
    return s

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    s = getSession(host=host,proxies=proxies)
    print(s.headers)