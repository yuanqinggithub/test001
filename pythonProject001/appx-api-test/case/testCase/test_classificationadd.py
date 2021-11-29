import os
import sys
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from case.func.classificationdelete import ClassificationDelete
from case.func.classificationadd import Classification
from common.read_yml import readyml
from common.operation_mysql import execute_sql
from common.logginger import logger

yamlPath = os.path.dirname(os.path.dirname(__file__)) + '/caseData/classificationadd.yml'
data = readyml(yamlPath)
classificationadd1 = data['classificationaddCase']

class TestClassification():
#     @pytest.fixture(scope='function')
#     def db_delete(self,operationmysql):
#         db = operationmysql
#         sql = '''
#         DELETE from classification_add where classification_name='{name}'
#         '''.format(name=data['classificationaddCase']['name'])
#         execute_sql(db,sql)
#         print('删除数据')


    @pytest.mark.parametrize('name',classificationadd1['name'])
    @pytest.mark.parametrize('parentId',classificationadd1['parentId'])
    @pytest.mark.parametrize('status',classificationadd1['status'])
    @pytest.mark.parametrize('source',classificationadd1['source'])
    # @pytest.mark.parametrize('name',['测试007'])
    # @pytest.mark.parametrize('parentId',['0'])
    # @pytest.mark.parametrize('status',['DEFAULT','DISABLED'])
    # @pytest.mark.parametrize('source',['APPX','RETAIL'])
    def test_classificationadd(self,getSession,getHostAndProxies,name,parentId,status,source):
        '''添加分类，只传必填项'''
        #db = operationmysql
        s=getSession
        host,proxies = getHostAndProxies
        data={
            'name': name,
            'parentId': parentId,
            'status': status,
            'source': source,
            'proxies':proxies
        }
        # sql = '''DELETE from classification_add where classification_name='{name}' '''
        r=Classification(s).classificationadd(**data)
        assert r['code'] == '000000'
        logger.info("添加分类成功")
        '''将分类删除'''
        classificationId=r['data']
        r1=ClassificationDelete(s).classificationDelete(classificationId,proxies=proxies)
        assert r1['code'] == '000000'
        logger.info("删除分类成功")
        # finally:
        #     sql = sql.format(name=name)
        #     logger.info('删除的sql:%s'%sql)
        #     execute_sql(db,sql)
        #     print('删除数据')



