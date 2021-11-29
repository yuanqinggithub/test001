import os
import sys
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
from case.func.getUserInfo import GetUserInfo

class TestGetUserInfo():
    host = 'https://backstageservices.dreawer.com'
    proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
    def test_getUserInfo(self,getSession):
        s=getSession
        #proxies = getHostAndProxies
        a=GetUserInfo(s)
        b=a.getUserInfo()
        assert b['code'] == '000000'



# if __name__ == '__main__':
#     from case.getSession import getSession
#     print(sys.path)
#     host = 'https://backstageservices.dreawer.com'
#     proxies = {
#         "http": "http://127.0.0.1:8888",
#         "https": "http://127.0.0.1:8888",
#     }
#     s = getSession(host=host,proxies=proxies)
#     info = GetUserInfo(s,host)
#     r = info.getUserInfo(proxies=proxies)
#     print(r)