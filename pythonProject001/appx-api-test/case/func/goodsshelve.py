import os
import sys
import requests
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#上架商品

class GoodsShelve():
    def __init__(self,s):
        self.s=s
        self.url ='https://backstageservices.dreawer.com/gc/goods/shelve'

    def goodsshelve(self,ids,proxies=None):
        data={
            'ids':[ids]
        }
        r=self.s.post(url=self.url,json=data,verify=False, proxies=proxies).json()
        return r
