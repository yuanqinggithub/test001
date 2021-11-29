import os
import sys
import urllib3
urllib3.disable_warnings()
sys.path.append('../../')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from case.func.uploadImage import UploadPhoto


class GoodsAdd():
    def __init__(self,s):
        self.s=s
        self.url = 'https://backstageservices.dreawer.com/gc/goods/add'
    def goodsadd(self,
                 storeId,
                 name,
                 categoryId,
                 stockType,
                 mainFigure,
                 service,
                 status,
                 recommend,
                 source,
                 classificationIds,
                 skus,
                 goodsPropertyNames,
                 freightParam,
                 allowRefund,
                 express,
                 cityDistribution,
                 selfPickUp,
                 detail,
                 proxies
                 ):
        data={
            'storeId': storeId,
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

    # def goodsadd(self,storeId,
    #              name,
    #              categoryId,
    #              mainFigure,
    #              status,
    #              recommend,
    #              source,
    #              classificationIds,
    #              troduction=None,
    #              detail=None,
    #              service=None,
    #              type=None,
    #              hidden=None,
    #              tradeIds=None,
    #              video=None,
    #              remark=None,
    #              skus=None,
    #              goodsPropertyNames=None,
    #              freightParam=None,
    #              miniapps=None,
    #              tdkTitle=None,
    #              tdkKeyword=None,
    #              tdkDescription=None,
    #              express=None,
    #              cityDistribution=None,
    #              selfPickUp=None,
    #              proxies=None
    #              ):
    #     data={  'storeId':storeId,
    #             'name':name,
    #             'categoryId':categoryId,
    #             'mainFigure':mainFigure,
    #             'status':status,
    #             'recommend':recommend,
    #             'source':source,
    #             'classificationIds':classificationIds,
    #             'troduction':troduction,
    #             'detail':detail,
    #             'service':service,
    #             'type':type,
    #             'hidden':hidden,
    #             'tradeIds':tradeIds,
    #             'video':video,
    #             'remark':remark,
    #             'skus':skus,
    #             'goodsPropertyNames':goodsPropertyNames,
    #             'freightParam':freightParam,
    #             'miniapps':miniapps,
    #             'tdkTitle':tdkTitle,
    #             'tdkKeyword':tdkKeyword,
    #             'tdkDescription':tdkDescription,
    #             'express':express,
    #             'cityDistribution':cityDistribution,
    #             'selfPickUp':selfPickUp,
    #             'proxies':proxies}
        r = self.s.post(url=self.url, json=data, verify=False, proxies=proxies).json()
        return r
