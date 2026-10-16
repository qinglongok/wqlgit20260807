import json
import re
import subprocess
import requests
import time
import hashlib

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
cookies = {
    "buvid3": "1DC67C2C-7251-8F41-5E29-88FC77B30CB313166infoc",
    "b_nut": "1788791013",
    "_uuid": "E10A49B55-33C6-91057-C8B5-E5A91084AF101213770infoc",
    "buvid_fp": "b3793fcf0f8725df512332cb740e1fb4",
    "buvid4": "6B71A621-3DFB-7F03-FC1A-7770BBED170E14530-026090722-0sKtBcpmr0kn9yBqdxHKSQ%3D%3D",
    "rpdid": "|(u)~|uRlmu)0J'u~)mJ~kkY)",
    "DedeUserID": "3747522874969346",
    "DedeUserID__ckMd5": "233b6b9735a1ac4c",
    "theme-tip-show": "SHOWED",
    "theme-avatar-tip-show": "SHOWED",
    "home_feed_column": "5",
    "SESSDATA": "78e6c48b%2C1807551624%2C1b9f4%2Aa1CjB4Qg-P7cLlWPeUIblIA1MhjkQ9O27jEcMcAlEai9xPYNtG9BTzkgslUXLktGoqBDsSVkpEX2wwNXlZTUVaZE8zMkQ3d3JLZkNlUVpZblBfeEJSQ1lNWlF4MU9BMmljLTlTdmNCdUE1dTlYTFZLZ2Vpc2thdmpFeElMNkdpeWF2dU9PQThQTG1BIIEC",
    "bili_jct": "8fdf96f0cd91309db67f6de41abac4d2",
    "CURRENT_QUALITY": "0",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTIzNTMxODAsImlhdCI6MTc5MjA5MzkyMCwicGx0IjotMX0.MOCYxyuKbfQRu6IlTZFz6QxfFLPOoEjC2DvrT-tPhBQ",
    "bili_ticket_expires": "1792353120",
    "browser_resolution": "1707-825",
    "bp_t_offset_3747522874969346": "1259845780592656384",
    "bsource": "search_bing",
    "sid": "5s7j0t0c",
    "CURRENT_FNVAL": "2000",
    "b_lsid": "6060ECE4_1A145F683C7"
}

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
    tittle = re.findall(r'data-title="(.*?)" title=',response.text)[0]
    print(tittle)
    res=re.findall(r'window.__playinfo__=(.*?)</script>', response.text)[0]
    print(res)
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
