import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time
import json
import re
params = {
    "tn": "resultjson_com",
    "ipn": "rj",
    "ct": "201326592",
    "is": "",
    "fp": "result",
    "queryWord": "美女",
    "cl": "2",
    "lm": "-1",
    "ie": "utf-8",
    "oe": "utf-8",
    "adpicid": "",
    "st": "-1",
    "z": "",
    "ic": "0",
    "hd": "",
    "latest": "",
    "copyright": "",
    "word": "美女",
    "s": "",
    "se": "",
    "tab": "",
    "width": "",
    "height": "",
    "face": "0",
    "istype": "2",
    "qc": "",
    "nc": "1",
    "fr": "",
    "expermode": "",
    "nojc": "",
    "pn": 0,
    "rn": 30,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Cookie':'BAIDUID=2B615EBB0625E565BB5CC10BDBDC6CD5:FG=1; BAIDUID_BFESS=2B615EBB0625E565BB5CC10BDBDC6CD5:FG=1'
    ,'Referer':'https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E7%BE%8E%E5%A5%B3'
}
number=1
for page in range(1,11):
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&word=%E7%BE%8E%E5%A5%B3&ie=utf-8&fp=result&fr=&ala=0&applid=10032807114973773114&pn={page*30}&rn=30&nojc=0&gsm=3c&newReq=1"
    resp = requests.get(url, headers=headers,params=params)
    # print(resp.status_code)
    try:
        # 清洗脏字符
        text = resp.text.replace(r"\'", "'")
        data = json.loads(text)
        img=data['data']['images']
        list1=[]
        for item in img:
            list1.append(item['thumburl'])
        # print(len(list1))
        # print(type(data))
        # print(data.keys())
        for url in list1:
            img_data = requests.get(url).content
            with open(f'images/{number}.png', mode='wb') as f:
                f.write(img_data)
            number+=1
        print(f'第{page}页爬取完成')
    # if isinstance(data, dict):
    #     print('字典解析成功')
    #     # img_list = data.get("data", [])
    #     # for item in img_list:
    #     #     # 注意大写 objURL
    #     #     obj_url = item.get("objURL")
    #     #     thumb_url = item.get("thumbURL")
    #     #     if obj_url:
    #     #         print("objURL:", obj_url)
    # else:
    #     print("解析后不是字典，接口被拦截！")
    except json.JSONDecodeError as e:
            print("JSON解析失败，返回不是JSON，百度拦截", e)
print('图片下载完成')


from dataclasses import field
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time
import json
import re
import pprint
import datetime
import csv
try:
    f=open('双色球.csv',mode='w',newline='')
    csv_writer=csv.DictWriter(f,fieldnames=[
          '期数',
          '开奖日期',
          '全国中奖详情',
          '红球',
          '蓝球',
          '奖池',
          '一等奖中奖注数',
          '一等奖中奖金额',
          '二等奖中奖注数',
          '二等奖中奖金额',
          '三等奖中奖注数',
          '三等奖中奖金额',
          '四等奖中奖注数',
          '四等奖中奖金额',
          '五等奖中奖注数',
          '五等奖中奖金额',
    ])
    csv_writer.writeheader()
except Exception as e:
    print(e)
for page in range(1,72):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'Cookie':'21_vq=6'
        ,'Referer':'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'
    }
    url='https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'
    num=1
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    params={
            'name':'ssq',
            'issueCount':'',
            'issueStart':'',
            'issueEnd':'',
            'dayStart':'2013-01-01',
            'dayEnd':date,
            'pageNo':page,
            'pageSize':'30',
            'week':'',
            'systemType':'PC',
    }
    resp = requests.get(url, headers=headers,params=params)
    try:
        text=resp.text.replace(r"\'", "'")
        result=resp.json()['result']
        for item in result:
            dic={
                '期数':item['code'],
                '开奖日期': item['date'],
                '全国中奖详情':item['content'],
                '红球':item['red'],
                '蓝球':item['blue'],
                '奖池':item['poolmoney'],
                '一等奖中奖注数':item['prizegrades'][0]['typenum'],
                '一等奖中奖金额':item['prizegrades'][0]['typemoney'],
                '二等奖中奖注数':item['prizegrades'][1]['typenum'],
                '二等奖中奖金额':item['prizegrades'][1]['typemoney'],
                '三等奖中奖注数':item['prizegrades'][2]['typenum'],
                '三等奖中奖金额':item['prizegrades'][2]['typemoney'],
                '四等奖中奖注数': item['prizegrades'][3]['typenum'],
                '四等奖中奖金额': item['prizegrades'][3]['typemoney'],
                '五等奖中奖注数': item['prizegrades'][4]['typenum'],
                '五等奖中奖金额': item['prizegrades'][4]['typemoney'],

            }
            csv_writer.writerow(dic)
    except Exception as e:
        print(e)
    print(f'第{page}页爬取完成')



