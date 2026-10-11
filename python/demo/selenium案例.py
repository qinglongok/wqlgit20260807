from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
opt = Options()
opt.add_experimental_option("detach", True)
diver=webdriver.Chrome(options=opt)
wait=WebDriverWait(diver,timeout=10)
diver.get("https://www.stats.gov.cn/sj/")
diver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form/div/input').send_keys("利润增长")
diver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form/div/button').click()
time.sleep(3)
handles = diver.window_handles
if len(handles)>1:
    diver.switch_to.window(handles[-1])
res = diver.page_source
soup = BeautifulSoup(res, 'lxml')
count=soup.find('div',class_='total-div')
if count:
    cnt=int(count.find('em').get_text())
    print(f'共有{cnt}条结果')
'''定义空列表接收爬取的json数据'''
all_data=[]
# page=int(input('请输入需要爬取页数：'))
# for i in range(1,page+1):
'''翻页爬取'''
for i in range(1,5):
    res = diver.page_source
    soup = BeautifulSoup(res, 'lxml')
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

    print(f'第{i}页爬取完成，目前爬取数据{len(all_data)}条，开始切换下一页...')
    '''切换至最新打开的页面'''
    diver.switch_to.window(handles[-1])
    '''定位到下一页按钮'''
    nxt = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="下一页"]')))
    diver.execute_script("arguments[0].scrollIntoView({block:'center'});", nxt)
    nxt.click()
    time.sleep(5)
print(f"完成{len(all_data)}条数据")
df = pd.DataFrame(all_data)
df.insert(0,"序号",range(1,len(df)+1))
df.to_csv('./爬取结果.csv',mode='w',index=False,encoding='utf-8-sig')
#     nxt = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="下一页"]')))
#     diver.execute_script("arguments[0].scrollIntoView({block:'end'});", nxt)
#     nxt.click()
#     time.sleep(2)
#     break
# s=diver.window_handles
# diver.switch_to.window(s[1]) #切换至刚打开的界面
# all_data=[]
# '''同时获取两个同级class的方法'''
# for i in range(10):
#     res = diver.page_source
#     soup = BeautifulSoup(res, 'lxml')
#     news=soup.find_all("div", class_="item-title")
#     for item in news:
#         news_time=item.find_next('div',class_='item-time')
#         if news_time:
#             res_a=item.find_all('a')
#             data1={
#                 "url": res_a[0]['href'],
#                 "title": res_a[0]['title'],
#                 "time":news_time.text
#             }
#             all_data.append(data1)
#     search=soup.find_all("div", class_="result-header-title")
#     for sech in search:
#         search_time=sech.find_next('div',class_='source-text')
#         if search_time:
#             res_b=sech.find_all('a')
#             data2={
#                 "url": res_b[0]['href'],
#                 "title": res_b[0]['title'],
#                 "time":search_time.text
#             }
#             all_data.append(data2)
#     df=pd.DataFrame(all_data)
#     df.insert(0,"序号",range(1,len(df)+1))
#     df.to_csv('./爬取结果.csv',mode='w',index=False,encoding='utf-8-sig')
#
#     print(df.head())
#
#     # class1=soup.find_all(attrs={'class':["item-title","item-time","result-header-title","source-text"]})
#     # for i in class1:
#     #     res_a=i.find_all('a')
#     #     url=res_a['href']
#     #     title=res_a['title']
#     #
#     #     print(res_a)
#     #     break
# #     # class2=class1.find_all(attrs={'class':["item-title","result-header-title"]})
#
# # diver.find_element(By.XPATH,'/html/body/div[12]/div/div[1]/div[3]/div/a[11]').click()
diver.quit()
