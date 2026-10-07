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
from lxml import etree
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=6e865502f18e6465891a0244a9f9842e,1791199005377; _ntes_nuid=6e865502f18e6465891a0244a9f9842e; Hm_lvt_1483fb4774c02a30ffa6f0e2945e9b70=1791199006; HMACCOUNT=753F32CC149A5777; WM_NI=d5J9bjt%2FSPPZ6KYW%2BGdsSZ%2FtwXn774jARdsI%2FyX7i3%2FJeB%2BdUOwQ0%2Bn%2FbqFHYSSz%2BoCbn%2BvUsp%2Fk8zYnohexHTganEeAjpUfPepCGHz5jOxuMxFZCgsfPECrZCrvfd%2Bbc3g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8cbc5a9ba99fa6f244af8a8ab3d14e938f8eb0cc4fb098abd6d77eb0edb6daf52af0fea7c3b92aa8eb86dae162b8f19db1d352f69597b8aa4da8ad9dbbae80b588a2d8b640aa9f9e85f243eda798d8ec39ed96aba3aa709791b9b2b321aef1ae92c5449b8d9d9baa6581bea2ccf55fb1b0e18cbb729bb2a189e8748c8ca982ed4fa79fa691d86e94bbc0a4c644baeba6b0fb7f8fa88abbc26db1baa0a6c27a9a9dbe97e570e9beadd4e637e2a3; WM_TID=8Tvmw8rPLvZFBBRRFVPIAgTa8C6x325u; NMTID=00O7LfqKksSDFPf60rxjUdfNYidMi4AAAGhC8fL-Q; WEVNSM=1.0.0; WNMCID=iphdic.1791199006853.01.0; ntes_utid=tid._.ucfZToEUWfVBA0VRVVOZEhSa4X6iSO1H._.0; sDeviceId=YD-SLYvwiPUQX5AAhVFQVKcFlSb5C%2FjSPgG; __snaker__id=61Gujn3Xhm7G94QO; gdxidpyhxdE=PIWc6nxuQ2xalVsXhr24KNz8et%5C5zTJTjgr0IZ0fmnT5wnn%2Bha13UDsaOlAcXIYlCaBP1SGAY98YaiSS%2FswNi1eb4UjluSYIUHlTum2xJQ%2BzGqlq5rJr063zUXQgjJ5tKVZXyXucPzToCMa5ZIEhRBS8Bfx8jBtD20YckakspCP1jCRv%3A1791206731986; MUSIC_U=00F943E338BDFD5E61A6622BC3DF93C406D509329FAE54D4B06A6961AFC272683987AE4C168F0176FB8FFBD1234721C074AF66C2FEC7271413760727CEED4A1D0E280EEA0AAE014B4D45EED851757E652D6A393AEFC040617BEB2F4AC50C2C69C12300EA3EA8906BE6237CC0B73652B8A7AC1C37400F59C72E6463014CAE6B9E9CB278AC1AEFBB5E2A2C86E7A3AF5F615BCF62C1A39444D70A9B768C25058AEBB2C37E616E89FCF06A364ADE1B84A94107420B6C69294261278B77019CB0021B5422FF8D2FC95240CBDD83EB14518AF0749090BA79A7F8F39E14A7BE3E9BA9FA2D4C3A54EF68601FF864BAC5AEFF7C9B6C27DE8AB1D8CFB1B4865948004844E273E45B7AD24B9B49B579227AF2706DE253A9EB2348981F7E00DFD2AEB1904BCEFDC9DC53FFC585AC3AE89598E92395428386148BBE5B8A174A57DB236CF5046E23275C61188467ED95294941139C9DC00785250EAA58DA3B5ED09C2DCC16DF4877342C71B52A44374400B14182D55688E91426C34E7E92F2DF2184D343DD93F2D1DF74B7915FA9C07F6300090E8923E3783719595506AC0CF69391E7B93ABC0766; __csrf=032f46c7ca52ca50692cf4520e4bcf85; ntes_kaola_ad=1; playerid=94846725; Hm_lpvt_1483fb4774c02a30ffa6f0e2945e9b70=1791216121; JSESSIONID-WYYY=gX6ThkEbTTGvotCwsEm3RcYQmYWNAe%2FheigHnU76DcGnhOPsMdgOKrnUwFIxwWZMfTuHahkbfSxSDVyUWE1V5JPCGvdA1X7lxs%2BuOCflGTTH0wphsQrz7oAdfAbQU1AtQ4NJFzIKwD90cbaQ1Mf%2F0UGiqpH4CvHW%5CjZ%2BnSGkHEh8VY7h%3A1791218133039'
    ,'Referer':'https://music.163.com/'
}

url='https://music.163.com/discover/toplist?id=3778678'
data={
    # 'params':'/w+dTgdjDwX+gOZ7TXr2WAtdKVCd7CSQsMRGZACNzU9n0OKj9Yhtw63XtdTwVx1GzYlAa67FIsDGIj8aDsyjG1QB4x9OSFqKadhze1ywrLGYvSkJ3WsfVrvj2dAD55AiKpCCyn6ryQmq8ePvlX4QUgCxALKCmgAJKO4JRyYksr0x9CE4m0WFdfuOVDPr5QKUo+fcu/GS+vvReE5CPkep9w=='
    # ,'encSecKey':'d2de73b7684ba5a3ea32b294a3586dce38dc0928bfd2c250c8df17a579980d42a8a36b0090bce8cd66e07abd70b7c98202fc8c05c46fc6d1bbfb648d3a83ac45cc8b4761ff169eea53fa6cae85e06ec3e9ef33ded7442baf3c39c0c9c390fc5272b72a2c2a9481601efcfa55ffede3a10a7d11365e58d3971528527fcb764973'
    #
    # 'vuutv':'YaQJ3vDUEn6Vt o/IhOZiu95nrZ2lrdyDOiCvIWByaaDLI6KuHZeY9EYR7DNSlMB90w/YbWSxRV3bCHGhGfSlRxK9SUs9gXmi1isx0ygEzg='
    # ,'authSecret':'000001a10c6bf5501e160ab0cb470007'
    'params':'8zRLQGlF4zHkrbfNM6E5jQd7x3UmuQjAEr3CdaRW75NvOxVrPRnnBqtBsf4PJUwsHS6bSI7qtXFCorPlRqRJx5HLVAbk6izo5nX23tqKmI+gNVE91bDf7wiYJr4RwcxLKyYxkPG8nhxbs5inWgu9ObpA+J4Lti2WWmyzIotDyOWawGCYjTwsmQ4/x5zqk64t7d1TH4q4UtWCLRkf89pdwA=='
    ,'encSecKey':'9f17b21e35d4d7978dc8394815ab53867821d39af8a6b94f8407724707fca138ce9e06970d2b435668e027e38d543d1517ec9256d2efb84223b7f349805e9fbc34ad180b54bbeaf3a0707459c91d3e114aa6c4b249ffd898cb34cbd28d8abd7f33ab27afa466b7e515ee43afce715772b073aa702a8c227c649d588680ee712c'
}
response=requests.get(url,headers=header)
text=response.text
html=etree.HTML(text)
li_list=html.xpath('//ul[@class="f-hide"]/li')
for item in li_list:
    song_name=item.xpath('./a/text()')[0]
    print(song_name)
    song_id=item.xpath('./a/@href')[0].split('=')[1]
    print(song_id)
    dit={
        song_name:song_id
    }
    print(dit)
# response=requests.post(url,headers=header)
# print(response.text)
# data_json=response.json()
# music_url=data_json['data'][0]['url']
# music_content=requests.get(music_url,headers=header).content
# with open('./music/岁月落笔写春秋.mp3','wb') as f:
#     f.write(music_content)


# try:
#     with open(f'./music/{song_name}.mp3','wb') as f:
#         f.write()
# except Exception as e:
#      print(e)

'''
 var bVn6a = window.asrsea(JSON.stringify(i2a), bxr4S(["流泪", "强"]), bxr4S(BH2i.md), bxr4S(["爱心", "女孩", "惊恐", "大笑"]));
e4u.data = j4S.cq8W({
    params: bVn6a.encText,
    encSecKey: bVn6a.encSecKey
    
i2a={
    "logs":"[{"action":"page",
              "json":{"page":"page_search_suggest",
                      "keyword":"周杰伦",
                      "rootpage":"page_search_result",
                      "mainsite":"1",
                      "mainsiteWeb":"1"
                      }
              }
             ]",
    "csrf_token": "032f46c7ca52ca50692cf4520e4bcf85"
}

'''


print(os.getcwd())