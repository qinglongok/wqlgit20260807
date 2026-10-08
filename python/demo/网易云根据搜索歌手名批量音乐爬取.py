import requests,execjs,math,time,os

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=6e865502f18e6465891a0244a9f9842e,1791199005377; _ntes_nuid=6e865502f18e6465891a0244a9f9842e; Hm_lvt_1483fb4774c02a30ffa6f0e2945e9b70=1791199006; HMACCOUNT=753F32CC149A5777; WM_NI=d5J9bjt%2FSPPZ6KYW%2BGdsSZ%2FtwXn774jARdsI%2FyX7i3%2FJeB%2BdUOwQ0%2Bn%2FbqFHYSSz%2BoCbn%2BvUsp%2Fk8zYnohexHTganEeAjpUfPepCGHz5jOxuMxFZCgsfPECrZCrvfd%2Bbc3g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8cbc5a9ba99fa6f244af8a8ab3d14e938f8eb0cc4fb098abd6d77eb0edb6daf52af0fea7c3b92aa8eb86dae162b8f19db1d352f69597b8aa4da8ad9dbbae80b588a2d8b640aa9f9e85f243eda798d8ec39ed96aba3aa709791b9b2b321aef1ae92c5449b8d9d9baa6581bea2ccf55fb1b0e18cbb729bb2a189e8748c8ca982ed4fa79fa691d86e94bbc0a4c644baeba6b0fb7f8fa88abbc26db1baa0a6c27a9a9dbe97e570e9beadd4e637e2a3; WM_TID=8Tvmw8rPLvZFBBRRFVPIAgTa8C6x325u; NMTID=00O7LfqKksSDFPf60rxjUdfNYidMi4AAAGhC8fL-Q; WEVNSM=1.0.0; WNMCID=iphdic.1791199006853.01.0; ntes_utid=tid._.ucfZToEUWfVBA0VRVVOZEhSa4X6iSO1H._.0; sDeviceId=YD-SLYvwiPUQX5AAhVFQVKcFlSb5C%2FjSPgG; __snaker__id=61Gujn3Xhm7G94QO; gdxidpyhxdE=PIWc6nxuQ2xalVsXhr24KNz8et%5C5zTJTjgr0IZ0fmnT5wnn%2Bha13UDsaOlAcXIYlCaBP1SGAY98YaiSS%2FswNi1eb4UjluSYIUHlTum2xJQ%2BzGqlq5rJr063zUXQgjJ5tKVZXyXucPzToCMa5ZIEhRBS8Bfx8jBtD20YckakspCP1jCRv%3A1791206731986; MUSIC_U=00F943E338BDFD5E61A6622BC3DF93C406D509329FAE54D4B06A6961AFC272683987AE4C168F0176FB8FFBD1234721C074AF66C2FEC7271413760727CEED4A1D0E280EEA0AAE014B4D45EED851757E652D6A393AEFC040617BEB2F4AC50C2C69C12300EA3EA8906BE6237CC0B73652B8A7AC1C37400F59C72E6463014CAE6B9E9CB278AC1AEFBB5E2A2C86E7A3AF5F615BCF62C1A39444D70A9B768C25058AEBB2C37E616E89FCF06A364ADE1B84A94107420B6C69294261278B77019CB0021B5422FF8D2FC95240CBDD83EB14518AF0749090BA79A7F8F39E14A7BE3E9BA9FA2D4C3A54EF68601FF864BAC5AEFF7C9B6C27DE8AB1D8CFB1B4865948004844E273E45B7AD24B9B49B579227AF2706DE253A9EB2348981F7E00DFD2AEB1904BCEFDC9DC53FFC585AC3AE89598E92395428386148BBE5B8A174A57DB236CF5046E23275C61188467ED95294941139C9DC00785250EAA58DA3B5ED09C2DCC16DF4877342C71B52A44374400B14182D55688E91426C34E7E92F2DF2184D343DD93F2D1DF74B7915FA9C07F6300090E8923E3783719595506AC0CF69391E7B93ABC0766; __csrf=032f46c7ca52ca50692cf4520e4bcf85; ntes_kaola_ad=1; playerid=94846725; Hm_lpvt_1483fb4774c02a30ffa6f0e2945e9b70=1791216121; JSESSIONID-WYYY=gX6ThkEbTTGvotCwsEm3RcYQmYWNAe%2FheigHnU76DcGnhOPsMdgOKrnUwFIxwWZMfTuHahkbfSxSDVyUWE1V5JPCGvdA1X7lxs%2BuOCflGTTH0wphsQrz7oAdfAbQU1AtQ4NJFzIKwD90cbaQ1Mf%2F0UGiqpH4CvHW%5CjZ%2BnSGkHEh8VY7h%3A1791218133039'
    ,'Referer':'https://music.163.com/'
}
url = 'https://music.163.com/weapi/song/enhance/player/url/v1'
search_url='https://music.163.com/weapi/cloudsearch/get/web'
# keywords=str(input('请输入你需要下载的歌手的名字：'))
keywords=input('请输入需要查询的歌手名字：')
params = {
    "csrf_token": "032f46c7ca52ca50692cf4520e4bcf85"
}
search_p_e=execjs.compile(open('../js/网易云.js', 'r', encoding='utf-8').read()).call('get_p_e', keywords)
print(search_p_e)
data={
    "params":search_p_e['encText'],
    "encSecKey":search_p_e['encSecKey']
}
rsp=requests.post(url=search_url,data=data,headers=headers,params=params)
print(rsp.json())
# info=rsp.json()['result']['songs']
songcount=rsp.json()['result']['songCount']
print(songcount)
singer_id=rsp.json()['result']['songs'][0]['ar'][0]['id']
print(singer_id)
# os_path=os.getcwd()+f'/网易云歌曲/{keywords}/'
# if not os.path.exists(os_path):
#     os.makedirs(os_path)
seach_p_e=execjs.compile(open(r'D:\pycharm\js\网易2.js', 'r', encoding='utf-8').read())
id_p_e=execjs.compile(open(r'D:\pycharm\js\网易1.js', 'r', encoding='utf-8').read())
offset = 0
total_page=math.ceil(songcount/30)
for page in range(1,total_page+1):
    i2a= {
            "hlpretag": "<span class=\"s-fc7\">",
            "hlposttag": "</span>",
            "id":singer_id,
            "s":keywords,
            "type": "1",
            "offset": offset,
            "total": "false",
            "limit": "30",
            "csrf_token": "032f46c7ca52ca50692cf4520e4bcf85"
        }
    seach_pe=seach_p_e.call('get_p_e',i2a)
    data_page = {
        "params": seach_pe['encText'],
        "encSecKey": seach_pe['encSecKey']
    }
    rsp_page = requests.post(url=search_url, data=data_page, headers=headers, params=params)
    info = rsp_page.json()['result']['songs']
    if not info:
        print('当前无歌曲信息，结束！')
        break
    count=0
    for item in info:
        count += 1
        song_id=item['id']
        song_name=item['name']
        id_pe=id_p_e.call('get_p_e', song_id)
        data_id={
            "params": id_pe['encText'],
            "encSecKey": id_pe['encSecKey']
        }
        try:
            rsp_id=requests.post(url=url,data=data_id,headers=headers,params=params)
            musc_url=rsp_id.json()['data'][0]['url']
            if musc_url is None:
                print(f'{song_name}为会员歌曲，跳过！')
                continue
            else:
                down_rsp=requests.get(musc_url,headers=headers,params=params).content
                with open(fr'D:\pycharm\music\莫小檀/{song_name}.mp3','wb') as f:
                # with open(os_path+song_name+'.mp3', 'wb') as f:  自动创建文件夹
                    f.write(down_rsp)
                    print(f'第{page}页第{count}首《{song_name}》下载完成！')
        except Exception as e:
            print(e)
        time.sleep(0.3) #单首延时
    print(f'第{page}页完成！开始{page+1}页')
    offset += 30
    time.sleep(0.5)
print(f'共爬取{songcount}')
# id='473164055'
# bVn6a=execjs.compile(open('网易1.js', 'r',encoding='utf-8').read()).call('get_p_e',id)
# data = {
#     "params":bVn6a['encText'],
#     "encSecKey":bVn6a['encSecKey']
# }
# response = requests.post(url, headers=headers, cookies=cookies,params=params, data=data)
# muc_url=(response.json()['data'][0]['url'])
# print(muc_url)
# try:
#     with open(f'D:/pycharm/music/茶汤.mp3', 'wb') as f:
#         f.write(requests.get(muc_url).content)
# except Exception as e:
#     print(e)



