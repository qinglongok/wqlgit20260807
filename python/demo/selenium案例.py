from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
opt = Options()
opt.add_experimental_option("detach", True)
diver=webdriver.Chrome(options=opt)
diver.get("https://www.stats.gov.cn/sj/")
diver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form/div/input').send_keys("利润增长")
diver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form/div/button').click()
time.sleep(3)
s=diver.window_handles
diver.switch_to.window(s[1]) #切换至刚打开的界面
res=diver.page_source
soup = BeautifulSoup(res, 'lxml')
all_data=[]
'''同时获取两个同级class的方法'''
news=soup.find_all("div", class_="item-title")
for item in news:
    news_time=item.find_next('div',class_='item-time')
    if news_time:
        res_a=item.find_all('a')
        data1={
            "url": res_a[0]['href'],
            "title": res_a[0]['title'],
            "time":news_time.text
        }
        all_data.append(data1)
search=soup.find_all("div", class_="result-header-title")
for sech in search:
    search_time=sech.find_next('div',class_='source-text')
    if search_time:
        res_b=sech.find_all('a')
        data2={
            "url": res_b[0]['href'],
            "title": res_b[0]['title'],
            "time":search_time.text
        }
        all_data.append(data2)
df=pd.DataFrame(all_data)
df.insert(0,"序号",range(1,len(df)+1))
df.to_csv('./爬取结果.csv',mode='w',index=False,encoding='utf-8-sig')
print(df.head())
# class1=soup.find_all(attrs={'class':["item-title","item-time","result-header-title","source-text"]})
# for i in class1:
#     res_a=i.find_all('a')
#     url=res_a['href']
#     title=res_a['title']
#
#     print(res_a)
#     break
# class2=class1.find_all(attrs={'class':["item-title","result-header-title"]})
diver.quit()
