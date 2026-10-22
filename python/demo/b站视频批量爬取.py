import json
import re
import subprocess
import requests
import time
import hashlib
from DrissionPage import ChromiumPage as uc

'''自动获取cookie'''
web=uc()
web.get("https://www.bilibili.com/")
web.ele('css:#nav-searchform > div.nav-search-content > input').input('美女',clear=True)
web.ele('css:#nav-searchform > div.nav-search-btn > svg').click()
'''等待加载数据'''
time.sleep(3)
cookie=web.cookies().as_dict()
web.quit()

'''
！！！此处的headers和cookies必须换成自己电脑的！！！
'''
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.bilibili.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%A5%B3&from_source=webhistory_search&spm_id_from=333.1007&search_source=3&page=2&o=36",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
cookies =cookie
link = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
keyword=input('请输入关键字搜索：')
wts=int(time.time())
a=[
    "aid=755463200",
    "isGaiaAvoided=true",
    "need_view=1",
    "web_location=1315873",
    f"{wts}"
]
string=("&".join(a)+'ea1db124af3c7062474693fa704f4ff8')
w_rid=hashlib.md5(string.encode('utf-8')).hexdigest()

'''需要多页的可以在这里定义params 里的page 参数即可'''
params = {
    "category_id": "",
    "search_type": "video",
    "ad_resource": "5654",
    "__refresh__": "true",
    "_extra": "",
    "context": "",
    "page": "1",
    "page_size": "42",
    "pubtime_begin_s": "0",
    "pubtime_end_s": "0",
    "from_source": "webhistory_search",
    "from_spmid": "333.337",
    "platform": "pc",
    "highlight": "1",
    "single_column": "0",
    "keyword": keyword,
    "qv_id": "r9T6zew4iPpB9SfL62BucIhdTfPok5ZG",
    "source_tag": "3",
    "gaia_vtoken": "",
    "dynamic_offset": "36",
    "web_roll_page": "1",
    "web_location": "1430654",
    "x-bili-device-req-json": "{\"platform\":\"web\",\"device\":\"pc\",\"spmid\":\"333.337\",\"mobi_app\":\"web_cn\"}",
    "x-bili-locale-json": "{\"c_locale\":{\"language\":\"zh\",\"script\":\"Hans\"},\"always_translate\":false}",
    "w_rid": w_rid,
    "wts": wts
}
response = requests.get(link, headers=headers, cookies=cookies, params=params)
json_data=json.loads(response.text)
id_re=json_data['data']['result']
for item in id_re:
    bvid=item.get('bvid',"")
    print(bvid)
    url =f'https://www.bilibili.com/video/{bvid}/'
    params = {
        "spm_id_from": "333.337.search-card.all.click",
        "vd_source": "ff647c984589fac1c127d1b9d1defd50"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    tmp1 = re.findall(r'data-title="(.*?)" title=',response.text)
    tittle=tmp1[0] if tmp1 else keyword
    # print(tittle)
    res=re.findall(r'window.__playinfo__=(.*?)</script>', response.text)[0]
    print(res)
    if not res:
        continue
    json_data=json.loads(res)
    print(json_data)
    video=json_data['data']['dash']['video'][0]['baseUrl']
    print(f'视频：{video}')
    audio=json_data['data']['dash']['audio'][0]['baseUrl']
    print(f'音频：{audio}')
    video_content=requests.get(video,headers=headers).content
    audio_content=requests.get(audio,headers=headers).content
    with open(f"./music/mp3/{tittle}.mp4", "wb") as video_file:
        video_file.write(video_content)
    with open(f"./music/mp3/{tittle}.mp3", "wb") as audio_file:
        audio_file.write(audio_content)
    cmd=f"ffmpeg -hide_banner -i ./music/mp3/{tittle}.mp4 -i ./music/mp3/{tittle}.mp3 -c:v copy -c:a copy -y ./music/mp4/{tittle}.mp4"
    subprocess.run(cmd, shell=True)
