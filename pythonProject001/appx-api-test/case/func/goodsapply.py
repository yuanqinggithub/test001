import os
import sys
import requests
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#添加商品
class GoodsApply():
    def __init__(self,s):
        self.s=s
        self.url ='https://backstageservices.dreawer.com/gc/goods/apply'

    def goodsapply(self,ids,proxies=None):
        data={'ids':[ids]}
        r=self.s.post(url=self.url,json=data,verify=False, proxies=proxies).json()
        return r
if __name__ == '__main__':
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }

