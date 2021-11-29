import sys
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append('../..')

class GetUserToken():
    def __init__(self,s):
        self.s = s
        self.url = 'https://backstageservices.dreawer.com/ecmps/getUserToken'

    def getUserToken(self,appid,proxies=None):
        data = {'appId':appid}
        r = self.s.get(url=self.url,params=data,verify=False,proxies=proxies).json()
        return r

    def getToken(self,appid,proxies=None):
        r = self.getUserToken(appid=appid,proxies=proxies)
        real_token = r['data']['token']
        return real_token

if __name__ == '__main__':
    from case.func.login import Login
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    l = Login(s)
    token, appid = l.getTokenAndAppID(proxies=proxies)
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    getToken = GetUserToken(s)
    real_token = getToken.getToken(appid=appid,proxies=proxies)
    print(real_token)
