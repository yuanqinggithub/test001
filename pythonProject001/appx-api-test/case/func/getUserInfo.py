import os
import sys
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')


class GetUserInfo():
    def __init__(self, s):
        self.s = s
        self.url = 'https://backstageservices.dreawer.com/bsmc/user/getInfo'

    def getUserInfo(self,proxies=None):
        r = self.s.get(url=self.url,verify=False,proxies=proxies).json()
        return r