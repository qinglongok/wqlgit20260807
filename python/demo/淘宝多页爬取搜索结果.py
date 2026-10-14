from DrissionPage import ChromiumPage as uc
from DrissionPage.common import By
import time
import re
import json
import hashlib
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://s.taobao.com/",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
cookies = {
    "t": "0282ca50dc9618a38519a33fa0e09a9c",
    "thw": "cn",
    "wk_cookie2": "12cc98d83d21dcdf44e4fc417aeeeadf",
    "wk_unb": "UU6lTM8jpH6wmQ%3D%3D",
    "aui": "2641936378",
    "xlly_s": "1",
    "fastSlient": "1791914534939",
    "ariaDefaultTheme": "default",
    "ariaFixed": "true",
    "ariaReadtype": "1",
    "ariaoldFixedStatus": "false",
    "ariaStatus": "false",
    "mt": "ci=0_0",
    "_tb_token_": "569eeb7b03a7b",
    "cookie2": "167cbd34f04930cc817742e3badd3726",
    "cna": "WudPI3knlicCAW94KU4kg0bg",
    "3PcFlag": "1791918225532",
    "sgcookie": "E100C1J0wwOoudFApbxrdC4WBtLb%2B3vI2WdVhNaAcwco5SY9489UNfMtndEX2kGnNxA0ckJEVOse%2BOZnZfj3IxLw%2FwNLaGzpoFzBkLBKJms5nIadQK0hZMzz23IZxGo726%2Fi",
    "unb": "2641936378",
    "csg": "756ab1c9",
    "lgc": "%5Cu9F99lotv%5Cu7237%5Cu7684%5Cu7231",
    "cancelledSubSites": "empty",
    "cookie17": "UU6lTM8jpH6wmQ%3D%3D",
    "dnk": "sweetlikehello",
    "skt": "62fb1dcd72f99d34",
    "tracknick": "%5Cu9F99lotv%5Cu7237%5Cu7684%5Cu7231",
    "_l_g_": "Ug%3D%3D",
    "sg": "%E7%88%B186",
    "_nk_": "%5Cu9F99lotv%5Cu7237%5Cu7684%5Cu7231",
    "cookie1": "UNQ0XMsD5%2Bih84iRMe0T7mnAQegUyV6HkpB24M%2BLSqM%3D",
    "uc1": "cookie14=UoYXLfFvSPZA0A%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpczFp&pas=0",
    "sn": "",
    "uc3": "vt3=F8dD1fNQS4Ocab7puhE%3D&nk2=ogidTfGxSD5bhlXX&id2=UU6lTM8jpH6wmQ%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D",
    "existShop": "MTc5MTkxODIyOQ%3D%3D",
    "uc4": "nk4=0%40oArxoOth04qr903Mzt94WGlh2xTMtbs%3D&id4=0%40U2xo%2FHOZXdp9WqX0tQO1DDia6wJz",
    "_cc_": "WqG3DMC9EA%3D%3D",
    "sca": "f5a7b218",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "9a64991c559feb3e642f030fd762cb7a_1791935042400",
    "_m_h5_tk_enc": "d863f8c3a41dbe7ca2323e8ba5646849",
    "_3dtid": "OkKpyTfSQzlyU+pAFws1UV7hsbV/u35fd3Jjg6T5yUt4JnYOhRlqgrcgaTOn9NFg",
    "tfstk": "h12yuvVowx2lPsM-Qc2uXz5baYE-ZzvBdvg5iru0vXvCwYGELr0bF4ZSE2vURkw7Rs6_2KJN05wrKeZcPnDFhN61Cufo2vZ0AlFgmjmKo0voZ0jqicitKDm3-qcmjcToKv43mioEA2vnZXqDn0nIK24nKirmkDDnqyDh0o0xxZVMLyq7YB3dRVmvK-orZsZoumnY30lzju02fhg9YeE80u_yBoM-3Po_Ptvz7uVg-54c3LlYZoyE6JK9YiL9Lpa6A_70pyz8wl8c1-F73f24W3B0I9w4zYwXhZjPKrkmEJAyPZy4DYzr9dfUBOFQTP4y_OeYdoe4GJRcEw2E8kr8Lmo42dcsNt2vqjdp9bKx0Vs-tBdKZcoq5iSH9Bh8gmu1qsf..",
    "isg": "BLu7R-6yVQwTZGm-ZPI4PqFTSp8lEM8SUded4614l7rRDNvuNeBfYtnCJqxCGCcK"
}
url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
params = {
    "jsv": "2.7.4",
    "appKey": "12574478",
    "t": "1791928880815",
    "sign": "4573e8d7cb122ebb79b7b1932990bf33",
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "timeout": "10000",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp6",
    "data": "{\"appId\":\"34385\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc\\\",\\\"page\\\":1,\\\"n\\\":48,\\\"q\\\":\\\"%E5%9B%BE%E4%B9%A6\\\",\\\"qSource\\\":\\\"url\\\",\\\"pageSource\\\":\\\"a21bo.jianhua/a.search_.0\\\",\\\"channelSrp\\\":\\\"\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"p4pS\\\":null,\\\"categoryp\\\":\\\"\\\",\\\"ha3Kvpairs\\\":null,\\\"myCNA\\\":\\\"WudPI3knlicCAW94KU4kg0bg\\\",\\\"screenResolution\\\":\\\"1707x960\\\",\\\"viewResolution\\\":\\\"1286x853\\\",\\\"userAgent\\\":\\\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36\\\",\\\"couponUnikey\\\":\\\"\\\",\\\"subTabId\\\":\\\"\\\",\\\"np\\\":\\\"\\\",\\\"clientType\\\":\\\"h5\\\",\\\"isNewDomainAb\\\":\\\"false\\\",\\\"forceOldDomain\\\":\\\"false\\\"}\"}",
    "bx-ua": "fast-load"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
text = response.text
json_text=re.findall(r'mtopjsonp6\((.*)',text)[0][:-1]
json_data=json.loads(json_text)
count=json_data['data']['mainInfo']['totalResults']
print(count)
token="9a64991c559feb3e642f030fd762cb7a"
eI=int(time.time()*1000)#时间戳
all_data=[]
for page in range(1,6):
    print(f'第{page}页开始爬取')
    em_params={
        "device": "HMA-AL00",
        "isBeta": "false",
        "grayHair": "false",
        "from": "nt_history",
        "brand": "HUAWEI",
        "info": "wifi",
        "index": "4",
        "rainbow": "",
        "schemaType": "auction",
        "elderHome": "false",
        "isEnterSrpSearch": "true",
        "newSearch": "false",
        "network": "wifi",
        "subtype": "",
        "hasPreposeFilter": "false",
        "prepositionVersion": "v2",
        "client_os": "Android",
        "gpsEnabled": "false",
        "searchDoorFrom": "srp",
        "debug_rerankNewOpenCard": "false",
        "homePageVersion": "v7",
        "searchElderHomeOpen": "false",
        "search_action": "initiative",
        "sugg": "_4_1",
        "sversion": "13.6",
        "style": "list",
        "ttid": "600000@taobao_pc_10.7.0",
        "needTabs": "true",
        "areaCode": "CN",
        "vm": "nw",
        "countryNum": "156",
        "m": "pc",
        "page": page,
        "n": 48,
        "q": "%E5%9B%BE%E4%B9%A6",
        "qSource": "url",
        "pageSource": "a21bo.jianhua/a.search_.0",
        "channelSrp": "",
        "tab": "all",
        "pageSize": "50",
        "totalPage": "100",
        "totalResults": "3130901",
        "sourceS": "1",
        "sort": "_coefp",
        "bcoffset": "-13",
        "ntoffset": "0",
        "filterTag": "",
        "service": "",
        "prop": "",
        "loc": "",
        "start_price": None,
        "end_price": None,
        "startPrice": None,
        "endPrice": None,
        "categoryp": "",
        "ha3Kvpairs": None,
        "myCNA": "WudPI3knlicCAW94KU4kg0bg",
        "screenResolution": "1707x960",
        "viewResolution": "1286x4903",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
        "couponUnikey": "",
        "subTabId": "",
        "np": "",
        "clientType": "h5",
        "isNewDomainAb": "false",
        "forceOldDomain": "false"
    }
    data={
        "appId": "34385",
        "params": json.dumps(em_params,separators=(',',':')),
    }
    em_data=json.dumps(data,separators=(',',':'))
    string=(token + "&" + str(eI) + "&" + "12574478" + "&" +em_data)
    sign=hashlib.md5(string.encode('utf-8')).hexdigest()
    print(sign)
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
    params = {
        "jsv": "2.7.4",
        "appKey": "12574478",
        "t": eI,
        "sign": sign,
        "api": "mtop.relationrecommend.wirelessrecommend.recommend",
        "v": "2.0",
        "timeout": "10000",
        "type": "jsonp",
        "dataType": "jsonp",
        "callback": "mtopjsonp6",
        "data":em_data,
        "bx-ua": "fast-load"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    text = response.text
    json_text=re.findall(r'mtopjsonp6\((.*)',text)[0][:-1]
    json_data=json.loads(json_text)
    itemsArray=json_data['data']['itemsArray']
    for item in itemsArray:
        try:
            area=item['procity'].split(' ')
            if len(area)==2:
                province=area[0]
                city=area[1]
            else:
                province=area[0]
                city='暂无城市信息'
            dic={
                "标题":item['title'].replace("<span class=H>","").replace("</span>",""),
                "店铺":item['nick'],
                "价格": item['price'],
                "省份": province,
                "城市": city,
                "销售情况": item['realSales'],
                "商品ID": item['item_id'],
            }
            all_data.append(dic)
            print(dic)
        except:
            pass
    print(f'第{page}页爬取完成，共爬取{len(all_data)}条数据，开始第下一页')

df=pd.DataFrame(all_data)
df.insert(0,'序号',range(1,len(df)+1))
df.to_csv('./淘宝数据.csv',mode='w',index=False,encoding='utf-8-sig')
# json_data = json.loads(response.text)
# print(response.text)
# print(response)


# token="16f7af5cd6257d24b547b87246a8311c"
# eI=int(time.time()*1000)#时间戳
# eT="12574478"
# em.data={"appId":"34385","params":" w"}
# eE(token + "&" + eI + "&" + eT + "&" + em.data)
#
# em_params={
#     "device": "HMA-AL00",
#     "isBeta": "false",
#     "grayHair": "false",
#     "from": "nt_history",
#     "brand": "HUAWEI",
#     "info": "wifi",
#     "index": "4",
#     "rainbow": "",
#     "schemaType": "auction",
#     "elderHome": "false",
#     "isEnterSrpSearch": "true",
#     "newSearch": "false",
#     "network": "wifi",
#     "subtype": "",
#     "hasPreposeFilter": "false",
#     "prepositionVersion": "v2",
#     "client_os": "Android",
#     "gpsEnabled": "false",
#     "searchDoorFrom": "srp",
#     "debug_rerankNewOpenCard": "false",
#     "homePageVersion": "v7",
#     "searchElderHomeOpen": "false",
#     "search_action": "initiative",
#     "sugg": "_4_1",
#     "sversion": "13.6",
#     "style": "list",
#     "ttid": "600000@taobao_pc_10.7.0",
#     "needTabs": "true",
#     "areaCode": "CN",
#     "vm": "nw",
#     "countryNum": "156",
#     "m": "pc",
#     "page": 2,
#     "n": 48,
#     "q": "%E5%9B%BE%E4%B9%A6",
#     "qSource": "url",
#     "pageSource": "a21bo.jianhua/a.search_.0",
#     "channelSrp": "",
#     "tab": "all",
#     "pageSize": "50",
#     "totalPage": "100",
#     "totalResults": "3130901",
#     "sourceS": "1",
#     "sort": "_coefp",
#     "bcoffset": "-13",
#     "ntoffset": "0",
#     "filterTag": "",
#     "service": "",
#     "prop": "",
#     "loc": "",
#     "start_price": None,
#     "end_price": None,
#     "startPrice": None,
#     "endPrice": None,
#     "categoryp": "",
#     "ha3Kvpairs": None,
#     "myCNA": "WudPI3knlicCAW94KU4kg0bg",
#     "screenResolution": "1707x960",
#     "viewResolution": "1286x4903",
#     "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
#     "couponUnikey": "",
#     "subTabId": "",
#     "np": "",
#     "clientType": "h5",
#     "isNewDomainAb": "false",
#     "forceOldDomain": "false"
# }
#
# data={
#     "appId": "34385",
#     "params": json.dumps(em_params,separators=(',',':')),
# }
# em_data=json.dumps(data,separators=(',',':'))
# string=(token + "&" + str(eI) + "&" + "12574478" + "&" +em_data)
# sign=hashlib.md5(string.encode('utf-8')).hexdigest()
