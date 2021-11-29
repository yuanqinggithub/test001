import os
import sys
import requests
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class ClassificationDelete():
    def __init__(self,s):
        self.s=s
        self.url='https://backstageservices.dreawer.com/gc/classification/delete'

    def classificationDelete(self,classificationId,proxies=None):
        data = {
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "id": classificationId
        }
        r=self.s.post(url=self.url,json=data,verify=False,proxies=proxies).json()
        return r
