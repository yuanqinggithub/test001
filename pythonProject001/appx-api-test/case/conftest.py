import os
import sys
import requests
import pytest
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.func.login import Login
from case.func.getUserToken import GetUserToken
from common.read_yml import readyml


@pytest.fixture(scope='module')
def getSession():
   # host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
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

#数据库操作
@pytest.fixture(scope='session')
def operationmysql():
    yamlPath = os.path.dirname(__file__) + '/caseData/classificationadd.yml'
    data = readyml(yamlPath)
    dbinfo = data['db']
    return dbinfo

