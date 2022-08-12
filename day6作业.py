# 2.类封装五个接口
# login
import requests
import urllib3
urllib3.disable_warnings()

def login(host = 'https://backstageservices.dreawer.com',phoneNumber='15527060286',password = 'hbc23687',proxies=None,verify=None):
    url1  = host + '/ecmps/login'
    data1 = {
        "phoneNumber":phoneNumber,"password":password
    }
    r1 = requests.post(url1,json=data1,proxies=proxies,verify=verify)
    return r1.json()


def getLoginToken(proxies):
    r1 = login(proxies=proxies,verify=False)
    token = r1['data']['token']
    return token

def getUserToken(s,host = 'https://backstageservices.dreawer.com',proxies = None):
    url2 = host + '/ecmps/getUserToken'
    data = {'appId': '1514e1d61686438f95fa46f19070c126'}
    r2 = s.get(url2,params=data,proxies=proxies,verify=False)
    token = r2.json()['data']['token']
    print(token)
    return token

def getGoodsDetails(s,host = 'https://backstageservices.dreawer.com',proxies=None):#获取商品详情
    url3 = host + '/gc/goods/getDetails'
    js3 = {
        "storeId":"1514e1d61686438f95fa46f19070c126",
        "status":"DEFAULT",
        "pageInfo":
            {"pageNo":1,
             "pageSize":10
             }
    }
    # data = {
    #     'Content-Type': 'application/json;charset=UTF-8'
    # }
    r3 = s.post(url3,json=js3,proxies=proxies,verify=False)
    details = r3.text
    print(details)

def addGoods(s,host = 'https://backstageservices.dreawer.com',proxies=None):
    url4 = host + '/gc/goods/add'
    data = {
         "storeId":"1514e1d61686438f95fa46f19070c126",
         "name":"测试商品",
         "categoryId":"bedbdf24503b11e8a3bc7cd30abc",
         "stockType":"RESTRICTED",
         "mainFigure":"/resource/RETAIL/20220809/adfeb3bc093e40e9b6f3e2209bbf94af.png",
         "service":"Test",
         "status":"DEFAULT",
         "recommend":'true',
         "source":"RETAIL",
         "classificationIds":["03125bddd23544cb8fb59a971d9f4efb"],
         "skus":[{"stock":"1","salesVolume":1,"originalPrice":"1","price":"12"}],
         "goodsPropertyNames":[],
         "allowRefund":'true',
         "express":'false',
         "cityDistribution":'false',
         "selfPickUp":'true',
         "detail":'null'
    }
    r4 = s.post(url4,json=data,proxies=proxies,verify=False)
    cd = r4.status_code
    print(cd)
    return cd
proxies = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
s = requests.session()
token = getLoginToken(proxies=proxies)
h1 = {
    'appId': '1514e1d61686438f95fa46f19070c126',
    'Authorization': token
}
s.headers.update(h1)
print(token)
token = getUserToken(s,proxies=proxies)
h2 = {
    'Authorization': token
}
s.headers.update(h2)
print(token)
getGoodsDetails(s,proxies=proxies)
addGoods(s,proxies=proxies)

