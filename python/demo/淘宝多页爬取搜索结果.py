from DrissionPage import ChromiumPage as uc
from DrissionPage.common import By
import time
import re
import json
import hashlib
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote

web=uc()
web.get("https://www.taobao.com")
time.sleep(3)
'''获取最新cookie'''
cookie=web.cookies().as_dict()
web.quit()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://s.taobao.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
cookies = cookie
url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'

keyword=input('请输入需要搜索的商品名称：')
encode_keyword=quote(keyword, safe='')
print(encode_keyword)
pic_data = []
for page in range(1,6):
    token = cookies['_m_h5_tk'].split('_')[0]
    eI = int(time.time() * 1000)  # 时间戳
    em_params = {
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
        "q": encode_keyword,
        "qSource": "url",
        "pageSource": "a21bo.jianhua/a.search_hover.0",
        "channelSrp": "",
        "tab": "all",
        "pageSize": "50",
        "totalPage": "100",
        "totalResults": "404339",
        "sourceS": "0",
        "sort": "_coefp",
        "bcoffset": "",
        "ntoffset": "",
        "filterTag": "",
        "service": "",
        "prop": "",
        "loc": "",
        "start_price": None,
        "end_price": None,
        "startPrice": None,
        "endPrice": None,
        "itemIds": None,
        "p4pIds": None,
        "p4pS": None,
        "categoryp": "",
        "ha3Kvpairs": None,
        "myCNA": "WudPI3knlicCAW94KU4kg0bg",
        "screenResolution": "1707x960",
        "viewResolution": "1287x4529",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
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
    string = (token + "&" + str(eI) + "&" + "12574478" + "&" + em_data)
    sign = hashlib.md5(string.encode('utf-8')).hexdigest()
    params1 = {
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
        "data": em_data,
        "bx-ua": "fast-load"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params1)
    json_text=re.findall(r'mtopjsonp6\((.*)',response.text)[0][:-1]
    json_data=json.loads(json_text)
    pic_url=json_data['data']['itemsArray']
    if page==1:
        cnt=json_data['data']['mainInfo']['totalResults']
    '''女士内衣'''
    for item in pic_url:

            areas = item.get('procity','暂无城市信息').split(' ')
            if len(areas) == 2:
                province = areas[0]
                city = areas[1]
            else:
                province = areas[0]
                city = '暂无城市信息'
            dic={
                "标题":item.get('title','').replace("<span class=H>","").replace("</span>",""),
                "店铺":item.get('nick',''),
                "价格": item.get('price',''),
                "省份": province,
                "城市": city,
                "销售情况": item.get('realSales',''),
                "商品ID": item.get('item_id',''),
                "图片链接":item.get('pic_path',''),
                "商品链接": item.get('auctionURL', ''),
                }
            pic_data.append(dic)

    print(pic_data)
    if page!=5:
         print(f'第{page}页爬取完成，开始下一页')
    else:
         print(f'最后一页爬取完成')
df=pd.DataFrame(pic_data)
df.insert(0,'序号',range(1,len(df)+1))
df.to_csv('./淘宝数据.csv',mode='w',encoding='utf-8-sig',index=False)
print(f'搜索结果共{cnt}条数据,爬取结果{len(pic_data)}条')
