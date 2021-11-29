import os
import sys
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from case.func.classificationdelete import ClassificationDelete
from common.read_yml import readyml
from common.operation_mysql import execute_sql
#from common.logginger import logger
from case.func.getSession import getSession

# yamlPath = os.path.dirname(__file__) + '/caseData/classificationadd.yml'
# data = readyml(yamlPath)
# classificationadd1 = data['classificationaddCase']



class Classification():
    def __init__(self,s):
        self.s=s
        self.url='https://backstageservices.dreawer.com/gc/classification/add'

    def classificationadd(self,
                          name,
                          parentId,
                          status,
                          source,
                          sequence=None,
                          logo=None,
                          introduction=None,
                          url=None,
                          recommend=None,
                          remark=None,
                          proxies=None):
        data={  'name':name,
                'parentId':parentId,
                'status':status,
                'source':source,
                'sequence':sequence,
                'logo':logo,
                'introduction':introduction,
                'url':url,
                'recommend':recommend,
                'remark':remark,
                'proxies':proxies}

        r=self.s.post(url=self.url,json=data,verify=False,proxies=proxies).json()
        return r


if __name__ == '__main__':
        '''添加分类，只传必填项'''
        # db = operationmysql
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        s = getSession()
        data = {
            'name': '测试006',
            'parentId': '0',
            'status': 'DEFAULT',
            'source': 'APPX',
            'proxies': proxies
        }
        # sql = '''DELETE from classification_add where classification_name='{name}' '''
        r = Classification(s).classificationadd(**data)
        assert r['code'] == '000000'
        '''将分类删除'''
        classificationId = r['data']
        r1 = ClassificationDelete(s).classificationDelete(classificationId, proxies=proxies)
        assert r1['code'] == '000000'
