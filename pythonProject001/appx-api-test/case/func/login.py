import os
import sys
import re
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append('../..')
class Login():
    def __init__(self, s):
        self.s = s
        self.url = 'https://backstageservices.dreawer.com/ecmps/login'

    def login(self,phoneNumber,password,proxies=None):
        data = {"phoneNumber":phoneNumber,"password":password}
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies).json()
        return r

    def getTokenAndAppID(self,phoneNumber='15527060286',password='hbc23687',proxies=None):
        r = self.login(phoneNumber,password,proxies)
        token = r['data']['token']
        appid = r['data']['apps'][0]['appId']
        return token,appid

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    # proxies = {
    #     "http": "http://127.0.0.1:8888",
    #     "https": "http://127.0.0.1:8888",
    # }
    s = requests.session()
    l = Login(s,host)
    r=l.login(phoneNumber='15527060286',password='hbc23687')
    appId = re.findall('{"appId":"(.*?)"',r.text)
    token = re.findall('"token":"(.*?)"',r.text)
    print(appId[0],token[0])

    # token,appid = l.getTokenAndAppID(proxies=proxies)
    # print(token,appid)


