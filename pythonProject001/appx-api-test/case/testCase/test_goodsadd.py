import os
import sys
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.func.uploadImage import UploadPhoto
from case.func.goodsapply import GoodsApply
from case.func.goodsremove import GoodsRemove
from case.func.goodsshelve import GoodsShelve
from case.func.goodsadd import GoodsAdd
from common.logginger import logger

#添加商品
class TestGoodsAdd():

    def test_goodsadd(self,getSession,getHostAndProxies):
        s=getSession
        host,proxies=getHostAndProxies
        name='测试001'
        storeId='1514e1d61686438f95fa46f19070c126'
        categoryId='bed66011503b11e8a3bc7cd30abc'
        file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/image/111.jpg'
        # file_path='./111.jpg'
        mainFigure=UploadPhoto(s).uploadphoto(file_path)
        service='Test'
        status='DEFAULT'
        recommend='False'
        source='RETAIL'
        classificationIds=['ca90efc41743422a9e3fd6429a1e5bd2','86f94b0b2c3e4c789409410db66c9517']
        stockType='RESTRICTED'
        skus=[{
            "stock":"22",
            "salesVolume":1,
            "originalPrice":"33",
            "price":"11"}]
        goodsPropertyNames=[]
        freightParam={
        "type":"FIXED",
        "price":0,
        "freightTemplateId":""}
        allowRefund=True
        express=True
        cityDistribution=False
        selfPickUp=False
        detail=None
        proxies=proxies
        data = {'storeId': storeId,
                'name': name,
                'categoryId': categoryId,
                'stockType': stockType,
                'mainFigure': mainFigure,
                'service': service,
                'status': status,
                'recommend': recommend,
                'source': source,
                'classificationIds': classificationIds,
                'skus': skus,
                'goodsPropertyNames': goodsPropertyNames,
                'freightParam': freightParam,
                'allowRefund': allowRefund,
                'express': express,
                'cityDistribution': cityDistribution,
                'selfPickUp': selfPickUp,
                'detail': detail,
                'proxies': proxies}
        r=GoodsAdd(s).goodsadd(**data)
        assert r['code'] == '000000'
        logger.info("添加商品")
        #下架商品
        ids=r['data']
        a=GoodsApply(s).goodsapply(ids,proxies=proxies)
        assert  a['code'] == '000000'
        logger.info("下架商品")
        #上架商品
        b=GoodsShelve(s).goodsshelve(ids,proxies=proxies)
        assert b['code'] == '000000'
        logger.info("上架商品")
        # 下架商品
        ids = r['data']
        a = GoodsApply(s).goodsapply(ids, proxies=proxies)
        assert a['code'] == '000000'
        logger.info("重新下载商品")
        #删除商品
        c=GoodsRemove(s).goodsremove(ids,proxies=proxies)
        assert c['code'] == '000000'
        logger.info("s删除商品")
