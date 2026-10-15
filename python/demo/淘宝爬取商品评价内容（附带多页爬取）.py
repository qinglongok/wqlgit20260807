import requests
import re
import json
import time
import pandas as pd
import hashlib
from DrissionPage import ChromiumPage as uc

'''获取最新cookie，防止过期返回空值'''
web=uc()
web.get("https://www.taobao.com")
time.sleep(3)
cookie=web.cookies().as_dict()
'''构造请求头，定义cookie，url，params等参数'''
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://item.taobao.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
cookies = cookie
url = 'https://h5api.m.taobao.com/h5/mtop.taobao.rate.detaillist.get/6.0/'
'''去读数据文件中的商品id'''
# df=pd.read_csv('./淘宝数据.csv',encoding='utf-8')
# id=df.loc[:,'商品ID'][1]
'''测试cookie是否获取成功'''
token=cookies['_m_h5_tk'].split('_')[0]
print(token)
'''加密参数sign的组合逻辑'''
ts=int(time.time()*1000) #时间戳
s='12574478'
'''
ID可通过搜索结果提取,可自定义输入：
id=input('请输入商品id:')
'''
id="904335075299"#测试例
sign_data={
    "showTrueCount": False,
    "auctionNumId": id,
    "pageNo": 1,
    "pageSize": 30,
    "orderType": "",
    "searchImpr": "-8",
    "expression": "",
    "skuVids": "",
    "rateSrc": "pc_rate_list",
    "rateType": "",
    "foldFlag": "0"
}
'''将字典/列表数据转换为json字符串'''
em_data=json.dumps(sign_data,separators=(',',':')) #separators参数去掉，号：号后面的空格！否则影响后续md5计算，必须要求！！！
string=(token + "&" + str(ts) + "&" + s + "&" + em_data)
'''加密sign字段'''
sign=hashlib.md5(string.encode('utf-8')).hexdigest() #hexdigest()将输出结果转换成16进制字符串
'''传入请求参数构建params,包含t/sign/sign_data(翻页逻辑存在此参数中，需要翻页只需要修改PageNo参数即可)'''
params = {
    "jsv": "2.7.5",
    "appKey": "12574478",
    "t": ts,
    "sign": sign,
    "_bx-login": "new",
    "api": "mtop.taobao.rate.detaillist.get",
    "v": "6.0",
    "isSec": "0",
    "ecode": "1",
    "timeout": "20000",
    "dataType": "jsonp",
    "valueType": "string",
    "type": "jsonp",
    "callback": "mtopjsonp15",
    "data": em_data
}
'''发起请求'''
response = requests.get(url, headers=headers, cookies=cookies, params=params)
'''正则匹配请求内容，提取mtopjsonp15()中的内容'''
json_text=re.findall(r'mtopjsonp15\((.*)',response.text)[0][:-1]
json_data=json.loads(json_text)
comment=json_data['data']['rateList']
con=json_data['data']['foldCount']
commt_data=[]
for item in comment:
    if item.get('feedPicPathList', ''):
        cimg_url=",".join(item.get('feedPicPathList', ''))
    else:
        cimg_url='该评价暂无图片内容'
    dic={
        "评论内容":item.get('feedback',''),
        "评论时间": item.get('feedbackDate', ''),
        "图片连接": cimg_url,
    }
    commt_data.append(dic)
'''保存为csv文件'''
df=pd.DataFrame(commt_data)
df.insert(0,'序号',range(1,len(df)+1))
df['评论总数']=""
df.loc[df.index[0],"评论总数"]=con
df_sorted=df.sort_values(by='评论时间',ascending=False)
df.to_csv('./评论内容.csv',mode='w',index=False,encoding='utf-8-sig')
print(f'爬取完成，已保存！')