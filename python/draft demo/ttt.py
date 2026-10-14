
a=10
b=7
c=5
d=2
print(5/10)
c**=d
print(c)
e=a//b  # 1 取商
f=a%b  # 3 取余数
print(e)
print(f)

def pf(x):
    return x**2
a=5
if (a:=pf(a))>10:
    print('a被运用')
else:
    print('123')

rs='a是偶数' if a%2==0 else 'a是奇数'
print(rs)

#while 必须先指定一个控制变量
i=0
while i<10:
    print(i)
    i=i+1
import time
cnt=2
while cnt!=0:
    print(f'\r倒计时：{cnt}秒',end='')
    time.sleep(0.003)
    cnt-=1
print()
print('倒计时结束')




a=[1,2,3,4,5]
b=['a','b','c','d','e']
c=dict(zip(b,a))  #直接用zip
print(c)
d={k:v for k,v in zip(b,a)}  #字典推导式
print(d)

name=['钱丹','赵小杨','王箐','程度','高敏']
wk_y=[10,20,16,3,4]
dc={k:v for k,v in zip(name,wk_y)}
na='钱丹'
if na in name:
    wy=dc.get(na)

max=wk_y[0]
for n  in wk_y:
    if n>max:
        max=n
print(max)


import itertools
import tkinter as tk
def keymap(digt):
    key_map={
    '0':[' '],
    '1':['@',':','.','!'],
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z'],
}
    letter=[key_map[d] for d in digt]
    print(letter)
    cob=list(itertools.product(*letter))
    print(cob)
    comb=["".join(cmb) for cmb in cob]
    return comb #函数结果是return ,调用函数时需要打印才会显示结果
print(keymap('28'))

ls=[1,33,6,4,52,8,2]
max=ls[0]
min=ls[0]
for n in ls:
    if n>max:
        max=n
    if n<max:
        min=n
print(max)
print(min)

max=ls[0]
i=1
while i<len(ls):
    if ls[i]>max:
        max=ls[i]
    i=i+1  #注意不要放在if中
print(max)

import math
print(math.sin(math.radians(90)))  #需要转换成弧度


def end_month_cost(cnt,per_c):
    cost=cnt*per_c
    return cost
a=6
b=1550
res=end_month_cost(a,b)
print(f'月末成本是:{res}')

def add(x):
    sum=0
    i=1
    while i<=x:
        sum=sum+i
        i=i+1
    return sum
print(add(5))

def add1(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(add1(5))


def show_poem():
    print('''
    《青玉案·元夕》
      宋·辛弃疾
    东风夜放花千树，
    更吹落、星如雨。
    宝马雕车香满路，
    风箫声，玉壶光转，一夜鱼龙舞。
    蛾儿雪柳黄金缕。
    笑语盈盈暗香去。
    众里寻他千百度。
    蓦然回首，那人却在，灯火阑珊处。
    ''')
show_poem()

from docx import Document
path=r"C:\Users\qlok\Desktop\观潮.docx"
tet=Document(path)
for p in tet.paragraphs:
    print(p.text)
    time.sleep(0.2)

def doublenum(n):
    lst=[]
    for i in range(1,n+1):
        if i%2==0:
            lst.append(i)
            print(f'\r当前偶数为：{i}',end=' ')
    print()
    return lst
print(doublenum(20))

def total(numlist):
    total=0
    for i in numlist:
        total=total+i
    return total
print(total([1,2,5,6,9]))

def cacl(x,y):
    return x+y,x-y
a,b=cacl(1,2)
print(a)
print(b)
l2=list(cacl(1,2))
print(*l2)

#多条return语句，return语句可以出现在函数的任何位置
# 当执行到第一个return 时段程序结束，返回到调用程序
discount={'羽绒服':0.7,'卫衣':0.6,'T——shirt':0.9,'跑鞋':0.8}
def judge_dsicount(goods):
    if goods in discount: #字典只查键不查值
        return f'{goods}的折扣为：{discount[goods]}折'
    else:
        return f'{goods}无折扣！'
print(judge_dsicount('卫衣'))
print(judge_dsicount('休闲裤'))

def cosmetics_consumption_tax(cost,rate=0.3):
    '''化妆品税率为30%'''
    return cost*rate
print(cosmetics_consumption_tax(10000))


def students_info(name,number,sex='女',*hobby):
    print(f'昵称：{name}',end=' ')
    print('ID:%s'%number, end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby), end=' ')
    print()
students_info('风影月',32,'男',"钢琴",'读书','绘画')
students_info(number=55,name='水木冰') #昵称：水木冰 ID:55 性别：女 爱好：()
# 当不定长参数为空时是为空元组
a='又见苍山起苍黄'
print("{:=^40}".format(a))  #变量：填充符号 ^居中符号 总宽度 ：=^40

def students_info_1(name,number,sex='女',**hobby):
    print(f'昵称：{name}',end=' ')
    print('ID:%s'%number, end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
students_info_1("水木冰",55)
students_info_1("水木冰",58,hobby=('吉他','绘画'))
students_info_1("水木冰",58,hobby1='足球',hobby2='吉他')
students_info_1("水木冰",58,爱好1='足球',hobby2='吉他')
# 函数调用关键字参数时为：key=value,而不i是key:value,冒号形式会报错

def cosmetics_consumption_tax(cost,rate=0.3):
    '''化妆品税率为30%'''
    return cost*rate
print(cosmetics_consumption_tax(10000))
#lambda形式
tax=lambda cost,rate=0.3:cost*rate
print(tax(10000))



def power(x,y):
    return x**y
def mul(x,y):
    return x*y
def fun(a,b):
    print(f'{a}*{b}=',mul(a,b))
    print(f'{a}的{b}次方为：',power(a,b))
fun(2,3)

def features(name):
    a_ls=['猫','狗','鱼']
    for n in ls:
        if name not in a_ls:
            continue
        else:
            if name=='猫':
                return name+',喵喵'
            elif name=='狗':
                return name+',汪汪'
            elif name=='鱼':
                return name+',水里游'
    return f'没有找到：{name}'

def outer(func):
    def wrapper(*args,**kwargs):
        st=time.time()
        res=func(*args,**kwargs)
        time.sleep(2)
        et=time.time()
        ct=et-st
        print(f'程序运行耗费{ct}秒')
        return res
    return wrapper

@outer
def main(name):
    tx='开始'
    ex='结束'
    print('{:=^40}'.format(tx))
    print('开始寻找中'+"."*10)
    print(features(name))
    print('{:=^40}'.format(ex))
main('猫')


import datetime
import random
from typing import Self

import t1
def jiami(text):
    print(f'正在加密文字："{text}"')
    print('{0:=^30}'.format("加密密文"))
    shift =random.choice(range(1, 26)) #随机取加密位数
    print(f'本次加密偏移量为：{shift}')
    sctr = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            str=(chr((ord(char) -base-shift)%26+base))
            sctr.append(str)
        else:
            sctr.append(char)
    return ''.join(sctr)
a=jiami('i love you')
print(a)

def caesar_breaker(ciphertext):
    print(f"正在破解密文: '{ciphertext}'")
    print("-" * 40)

    # 遍历 1 到 25 的所有可能偏移量
    for shift in range(1, 26):
        decrypted = []
        for char in ciphertext:
            if char.isalpha():
                # 确定大小写的基准 ASCII 码
                base = ord('A') if char.isupper() else ord('a')
                # 核心解密公式：(当前字符 - 基准码 - 偏移量) % 26 + 基准码
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted.append(decrypted_char)
            else:
                # 非字母字符（如空格、标点）保持不变
                decrypted.append(char)

        print(f"偏移量 {shift:02d}: {''.join(decrypted)}")

secret_text = 't wzgp jzf' # 这是 "Hello World!" 偏移 3 位后的密文
caesar_breaker(secret_text)

# for char in secret_text:
# if char.isalpha():


a=30
print(f'{a:03d}')

print('{0:*^40}'.format("我们是冠军"))
print('{0:=^40}'.format("江南春"))

s ='banana'
print(s.count('a'))

print('{0:@^40}'.format('we are friend'))

n=[1,2,3,4,5]
res=list(filter(lambda x:x%2==0,map(lambda a:a**2,n)))
print(res)

from decimal import Decimal
def danli_interes():
    p=10000
    r=0.05
    n=3
    interes=p*r*n #复利利息计算
    return interes
res=Decimal(danli_interes()).quantize(Decimal('0.00'))
print(res)

def danli_income(p,r,n):
    m=p+p*r*n
    return round(m,2)
da=danli_income(10000,0.05,2)
print(da)

def danli_income(p,r,n=3):
    m=p+p*r*n
    return round(m,2)
da=danli_income(10000,0.05)
print(da)

rcs=lambda p,r,n:p+p*r*n
res1=rcs(10000,0.05,4)
print(res1)

class Public:
    name='lol'  #类属性
    def __init__(self,book):
        self.book=book  #实例属性
    def show(self):
        print(f'类的实例属性：{self.book}')
class  Publicinfo(Public):
    def showinfo(self):
        super().show()
d=Publicinfo('迪迦奥塔曼')
d.show()

class pf(object):
    def __init__(self):
        self.tc='唱歌'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
class pf1(pf):
    def __init__(self):
        self.tc = '跳舞'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
        super().__init__()
        super().mtd()
class pf2(pf1):
    def __init__(self):
        self.tc='下棋'
    def mtd(self):
        print(f'自己的技能是{self.tc}')
    def pf_m(self):      #将父类的属性值添加到自身属性里（多个时每个独立添加）
        pf.__init__(self)
        pf.mtd(self)
    def pf1_m(self):
        pf1.__init__(self)
        pf1.mtd(self)
    def toget(self):
        super().__init__()
        super().mtd()
#一次性调用多个父类属性方法  手动调用
#super函数
d5=pf2()
d5.mtd()
d5.toget()


def danli_pv(fv,n,r=0.01):
    pv=fv/(1+r*n)  #pv指当前本金值，fv指到期收益值，r利率，n期数
    return round(pv,2)

def fuli_pv(fv,n,r=0.01):
    pv=fv/(1+r)**n
    return round(pv,2)

def check_pick():
    fv = 10 #float(input('请输入到期希望获得的期望收益额：'))
    n =2 #float(input('请输入投资期数：'))
    res1=danli_pv(fv,n)
    res2=fuli_pv(fv,n)
    pick='单例方案优'if res1<res2 else '两种方案一样' if res1==res2 else '复利方案优'
    print(f'''
{"对比情况如下：":=^40}
期望收益{fv},
单利方案现在需投资{res1},
复利方案现在需投资{res2},
{pick}
        ''')
if __name__=='__main__':
    check_pick()


dl=danli_pv(100,0.02,3)
fl=fuli_pv(200,0.02,3)
print(f'单利理财投资额：{dl}')
print(f'复利理财投资额：{fl}')


# def pick_over():
#     global fvn
#     methd='1.单利投资,2.复利投资'
#     fv=float(input('请输入到期希望获得的期望收益额：'))
#     n=float(input('请输入投资期数：'))
#     while True:
#         print('{0:=^40}'.format(methd))
#         choice=input('请输入选择投资方式（1 ，2）？：\t\n')
#         if choice=='1':
#             res1=danli_pv(fv,r1,n)
#             print(res1)
#             break
#         elif choice=='2':
#             res2=fuli_pv(fv,r2,n)
#             print(res2)
#             break
#         else:
#             print('错误，请重新输入1或者2')
#     pick='单利投资理财方案优于复利投资方案'if res1>res2 else '两种方案一样' if res1==res2 else '复利方案优'
# if __name__=='__main__':
#     pick_over()

# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# url=r"https://www.zhcw.com/kjxx/ssq/kjxq/?kj"
# res=requests.get(url)
# print(res)
# soup=BeautifulSoup(res.text,'html.parser')
# table=soup.find('table',attrs={'[class](https://www.zhcw.com/c/2019-08-19/580211.shtml;kwd=class)':'t1'})
# rows=table.tbody.find_all('tr')
# for row in rows:
#     data=row.find_all('td')
#     if len(data)==0:
#         continue
#     issue_num=data[0].text
#     blue_ball=data[1].text
#     red_ball=data[2].text
#     print(issue_num,blue_ball,red_ball)

import time
# a="❤️"
# for i in range(10):
#     print(f"\r{i+1}/10",end="")
#     time.sleep(1)

# qian = "\033[38;2;72;209;204m"
# hou = "\033[38;2;238;238;238m"
# f_bg = '\u2588'
# e_bg = '\u2591'
# for i in range(101):
#     tt=i
#     bo=qian+f_bg*i
#     print(f'\r进度：{bo}{tt:.2f}%',end='')
#     time.sleep(0.05)

a="🐣"
for i in range(51):
    yi=(i/50)*100
    ht=a*i
    print(f'\r进度：{ht}{yi:.2f}%',end='')
    time.sleep(0.05)


def intro():
    print('{0:-^40}'.format('欢迎使用工作量计算程序'))
    print('Prompt: 程序需要选择你的计算类型')

def myinput():
    '''输入内容并根据需求计算对应的结果'''
    print(f'请选择你需要计算的类型：1-计算人均工时，2-计算人力数量，3-计算订单大小')
    choice=input('请输入你的计算类型：')
    if choice=='1':
        print('你选择的类型是计算人均工时，请输入订单大小（可以为小数）和人力数量（必须为整数）')
        print('请输入订单大小（1为标准大小，可以为小数')
        size=float(input('请输入你的订单大小，可以为小数：'))
        print('请输入人力数量（整数）')
        labour=int(input('请输入人力数量：'))
        hour=None
        return choice,size,labour,hour
    if choice=='2':
        print('你选择的类型是计算人力数量，请输入订单大小（可以为小数）和人均工时（可以为小数）')
        print('请输入订单大小（1为标准大小，可以为小数')
        size = float(input('请输入你的订单大小，可以为小数：'))
        labour = None
        print('请输入人均工时（可以为小数）')
        hour = float(input('请输入人均工时：'))
        return choice, size, labour, hour
    if choice=='3':
        print('你选择的类型是计算订单大小，请输入人力数量（必须为整数）和人均工时（可以为小数）')
        print('请输入订单大小（1为标准大小，可以为小数')
        size = None
        print('请输入人力数量(整数）')
        labour = int(input('请输入人力数量：'))
        print('请输入人均工时（可以为小数）')
        hour = float(input('请输入人均工时：'))
        return choice, size, labour, hour
def estimated(choice, size, labour, hour):
    if choice=='1':
        #计算人均工时
        hour=float(size*120/labour)
    elif choice=='2':
        #计算人力数量
        labour=int(math.ceil(size*120/hour))
    elif choice=='3':
        #计算订单大小
        size=round((hour*labour/120),1)
    return size,labour,hour

def summary(size,labour,hour):
    print(f'订单大小为{size}个标准订单，使用{labour}个人力完成，人均工时为：{hour}个')
    print('感谢使用，欢迎再会！')

def main():
    intro()
    choice,size,labour,hour=myinput()
    size,labour,hour=estimated(choice,size,labour,hour)
    summary(size,labour,hour)
main()


# 异常处理
import math
import time

try:
    res='a'>1
except Exception as e:
    print(f'出错了：{e}')

try:
    1==2
except:
    print('process exception')
else:
    print('success')

from docx import Document
try:
    path=r"C:\Users\qlok\Desktop\观潮.docx"
    doc=Document(path)
    files='\n'.join([p.text for p in doc.paragraphs])
    print(files)
except Exception as e:
    print(e)

try:
    openfiles=open('notExistsfile.txt','r')
    fileContent=openfiles.readlines()
except IOError:
    print('file not exists')
except Exception as e:
    print(e)
finally:
    print('执行最后的操作')



# import random
# def guess_num():
#     print('{0:-^30}'.format('猜数字游戏'))
#     cnt=0
#     try:
#         num=random.randint(1,100)
#         while 1==1:
#             try:
#                 n=int(input('请输入你猜的数字（1-100）：'))
#                 cnt += 1
#                 if n==num:
#                      print('{0:-^40}'.format(f'恭喜你猜对了,共猜了{cnt}次'))
#                      break
#                 elif n>num:
#                     print('大了')
#
#                 else:
#                      print('小了，请重新猜：')
#
#             except Exception as e:
#                   print(e)
#     except:
#         print('lolokol')
#     else:
#         print('执行完成')
# guess_num()


try:
    c="a"+1
except TypeError:
    print("语法错误，类型异常")

try:
    c='o'+1
except Exception as e:
    print(e)

try:
    5==1+2
except:
    print('process exception')
else:
    print('success')


try:
    print(b)
except SyntaxError as Se:
    print(Se)
except Exception as e:
    print(e)
finally:
    print('over')


path=r"C:\Users\qlok\Desktop\新建 文本文档.txt"
try:
    f=open(path,mode='a+',encoding='utf-8')
    c=f.read()
    print(c)
    com='原来，循环往复是生活的本质所在，一切似曾相识并不是错觉，是你转阿转阿转，最后又回到出发时的模样而已\n'
    f.write(com)
    f.close()
except Exception as e:
    print(e)
else:
    print('ok')

import os
rp=os.path.abspath('笔记py.txt')
ho=os.path.exists(rp)
print(ho)
print(rp)


path=r'C:\Users\qlok\Desktop\新建 文本文档.txt'
f=open(path,mode='r',encoding='utf-8')
conl=f.read()
print(conl)
f.close()

f2=open(path,mode='a+',encoding='utf-8')
con2='i am hero'
f2.write(con2)
f2.close()

import os
# os.makedirs('test/temp')
# open('test/temp/test.txt','w+').close()
if os.path.exists('test/temp/test.txt'):
    print('存在')
else:
    print('没有')

a=200/120
print(f'{a:.1f}')


import sqlite3
import random
from encodings import utf_8
from unittest import case

conn = sqlite3.connect('qlok.db')
cursor = conn.cursor()
addrs=[
    "北京市朝阳区建国路88号",
    "上海市浦东新区张江高科技园区博云路2号",
    "广东省深圳市南山区科技园高新南一道",
    "浙江省杭州市西湖区文三路478号",
    "江苏省南京市鼓楼区中山北路217号",
    "四川省成都市武侯区武侯祠大街188号",
    "湖北省武汉市洪山区珞喻路1037号",
    "陕西省西安市雁塔区雁塔西路76号",
    "山东省济南市历下区经十路9777号",
    "辽宁省沈阳市和平区青年大街374号",
    "湖南省长沙市岳麓区麓山南路932号",
    "福建省厦门市思明区厦大南路1号",
    "河南省郑州市金水区农业路63号",
    "云南省昆明市五华区一二一大街298号",
    "贵州省贵阳市观山湖区林城西路95号"
]
list_id=[]
id_list=cursor.execute("select id from users").fetchall()
for id in id_list:
    list_id.append(id[0])
for uid in list_id:
    addr=random.choice(addrs)
    sql='''
    update users
    set remark=case id%2 when 0  then 'this is china' else 'other land territory' end;'''
    cursor.execute(sql)
conn.commit()
conn.close()

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
import execjs

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=6e865502f18e6465891a0244a9f9842e,1791199005377; _ntes_nuid=6e865502f18e6465891a0244a9f9842e; Hm_lvt_1483fb4774c02a30ffa6f0e2945e9b70=1791199006; HMACCOUNT=753F32CC149A5777; WM_NI=d5J9bjt%2FSPPZ6KYW%2BGdsSZ%2FtwXn774jARdsI%2FyX7i3%2FJeB%2BdUOwQ0%2Bn%2FbqFHYSSz%2BoCbn%2BvUsp%2Fk8zYnohexHTganEeAjpUfPepCGHz5jOxuMxFZCgsfPECrZCrvfd%2Bbc3g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8cbc5a9ba99fa6f244af8a8ab3d14e938f8eb0cc4fb098abd6d77eb0edb6daf52af0fea7c3b92aa8eb86dae162b8f19db1d352f69597b8aa4da8ad9dbbae80b588a2d8b640aa9f9e85f243eda798d8ec39ed96aba3aa709791b9b2b321aef1ae92c5449b8d9d9baa6581bea2ccf55fb1b0e18cbb729bb2a189e8748c8ca982ed4fa79fa691d86e94bbc0a4c644baeba6b0fb7f8fa88abbc26db1baa0a6c27a9a9dbe97e570e9beadd4e637e2a3; WM_TID=8Tvmw8rPLvZFBBRRFVPIAgTa8C6x325u; NMTID=00O7LfqKksSDFPf60rxjUdfNYidMi4AAAGhC8fL-Q; WEVNSM=1.0.0; WNMCID=iphdic.1791199006853.01.0; ntes_utid=tid._.ucfZToEUWfVBA0VRVVOZEhSa4X6iSO1H._.0; sDeviceId=YD-SLYvwiPUQX5AAhVFQVKcFlSb5C%2FjSPgG; __snaker__id=61Gujn3Xhm7G94QO; gdxidpyhxdE=PIWc6nxuQ2xalVsXhr24KNz8et%5C5zTJTjgr0IZ0fmnT5wnn%2Bha13UDsaOlAcXIYlCaBP1SGAY98YaiSS%2FswNi1eb4UjluSYIUHlTum2xJQ%2BzGqlq5rJr063zUXQgjJ5tKVZXyXucPzToCMa5ZIEhRBS8Bfx8jBtD20YckakspCP1jCRv%3A1791206731986; MUSIC_U=00F943E338BDFD5E61A6622BC3DF93C406D509329FAE54D4B06A6961AFC272683987AE4C168F0176FB8FFBD1234721C074AF66C2FEC7271413760727CEED4A1D0E280EEA0AAE014B4D45EED851757E652D6A393AEFC040617BEB2F4AC50C2C69C12300EA3EA8906BE6237CC0B73652B8A7AC1C37400F59C72E6463014CAE6B9E9CB278AC1AEFBB5E2A2C86E7A3AF5F615BCF62C1A39444D70A9B768C25058AEBB2C37E616E89FCF06A364ADE1B84A94107420B6C69294261278B77019CB0021B5422FF8D2FC95240CBDD83EB14518AF0749090BA79A7F8F39E14A7BE3E9BA9FA2D4C3A54EF68601FF864BAC5AEFF7C9B6C27DE8AB1D8CFB1B4865948004844E273E45B7AD24B9B49B579227AF2706DE253A9EB2348981F7E00DFD2AEB1904BCEFDC9DC53FFC585AC3AE89598E92395428386148BBE5B8A174A57DB236CF5046E23275C61188467ED95294941139C9DC00785250EAA58DA3B5ED09C2DCC16DF4877342C71B52A44374400B14182D55688E91426C34E7E92F2DF2184D343DD93F2D1DF74B7915FA9C07F6300090E8923E3783719595506AC0CF69391E7B93ABC0766; __csrf=032f46c7ca52ca50692cf4520e4bcf85; ntes_kaola_ad=1; playerid=94846725; Hm_lpvt_1483fb4774c02a30ffa6f0e2945e9b70=1791216121; JSESSIONID-WYYY=gX6ThkEbTTGvotCwsEm3RcYQmYWNAe%2FheigHnU76DcGnhOPsMdgOKrnUwFIxwWZMfTuHahkbfSxSDVyUWE1V5JPCGvdA1X7lxs%2BuOCflGTTH0wphsQrz7oAdfAbQU1AtQ4NJFzIKwD90cbaQ1Mf%2F0UGiqpH4CvHW%5CjZ%2BnSGkHEh8VY7h%3A1791218133039'
    , 'Referer': 'https://music.163.com/'
}
serch_url = 'https://music.163.com/weapi/cloudsearch/get/web'
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=032f46c7ca52ca50692cf4520e4bcf85'
link_url = 'https://music.163.com/playlist?id=720487191'
response = requests.get(link_url, headers=header)
text = response.text
html = etree.HTML(text)
li_list1 = re.findall(r'a href="/song\?id=(\d+)">(.*?)</a>', text)
for song_id, name in li_list1:
    p_e = execjs.compile(open(r'/js/网易1.js', 'r').read()).call('get_p_e', song_id)
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=032f46c7ca52ca50692cf4520e4bcf85'
    data = {
        "params": p_e['encText'],
        "encSecKey": p_e['encSecKey']
    }
    response1 = requests.post(url, headers=header, data=data)
    json_data = response1.json()
    msc_url = json_data['data'][0]['url']
    if msc_url is None:
        print('{0:=^40}'.format(f'会员歌曲：《{name}》，已经跳过'))
    else:
        msc_content = requests.get(msc_url, headers=header).content
        try:
            with open(fr'D:\pycharm\music\{name}.mp3', 'wb') as f:
                f.write(msc_content)
                print('{0:=^40}'.format(f'非会员歌曲：《{name}》，下载完成！'))
        except Exception as e:
            print(e)

# li_list=html.xpath('//ul[@class="f-hide"]/li')
# for item in li_list:
#     song_name=item.xpath('./a/text()')[0]
#
#     song_id=item.xpath('./a/@href')[0].split('=')[1]
#
#     dit={
#         song_name:song_id
#     }
#     print(dit)
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




csrf_token:"032f46c7ca52ca50692cf4520e4bcf85"
limit:"8"
s:"周杰伦"

{
    "hlpretag": "<span class=\"s-fc7\">",
    "hlposttag": "</span>",
    "s": "周杰伦",
    "type": "1",
    "offset": "0",
    "total": "true",
    "limit": "30",
    "csrf_token": "032f46c7ca52ca50692cf4520e4bcf85"
}

{
    "hlpretag": "<span class=\"s-fc7\">",
    "hlposttag": "</span>",
    "id": "3695",
    "s": "李健",
    "type": "1",
    "offset": "60",
    "total": "false",
    "limit": "30",
    "csrf_token": "032f46c7ca52ca50692cf4520e4bcf85"
}
'''



from DrissionPage import ChromiumPage as uc
import time
import re
# opt = Options()
# opt.add_experimental_option("detach", True)
#创建浏览器对象，设置超时/重试
page= uc()
page.listen.start('h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0')
page.get("https://www.taobao.com/")
page.ele('xpath://*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
# page.ele('xpath://*[@id="q"]').input('内裤')
# page.ele('xpath://*[@id="J_TSearchForm"]/div[2]/button').click()
ele=page.ele('xpath://*[@id="fm-login-id"]').clear()
ele.input("15286524744")
page.ele("#fm-login-password").input("qlok996")
# page.ele('xpath://*[@id="fm-login-id"]').input('15286524744')
# page.ele('xpath://*[@id="fm-login-password"]').input('qlok996')
page.ele('xpath://*[@id="login-form"]/div[7]/button').click()
page.ele('xpath:/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
#直接在内容后面加回车
page.ele('xpath://*[@id="q"]').input("女士内衣")
page.ele('xpath://*[@id="J_TSearchForm"]/div[2]/button').click()
res=page.listen.wait().response
data_json=re.findall(r'mtopjsonp\d+\((.*)\)',res.body)
print(data_json)

# page.ele('xpath://*[@id="chat-textarea"]').input('牛顿\n')
#输入后点击百度一下按钮
# page.ele('xpath://*[@id="chat-textarea"]').input('利润增长')
# page.ele('xpath://*[@id="chat-submit-button"]').click()
# diver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/div[2]/textarea').send_keys("利润增长",Keys.ENTER)
# time.sleep(3)
# # next-icon next-icon-arrow-right next-xs next-btn-icon next-icon-last next-pagination-icon-next" data-spm-anchor-id="a21n57.1.0.i0.2e1c31f6biI9wQ"></i>
# scroll_box = page.ele("#search-content-leftWrap", timeout=5)
# scroll_box.scroll.down(4200)

# page.ele('xpath:/*[@id="search-content-leftWrap"]/div[3]/div[6]/div/div/button[2]/span').click()
# s=diver.window_handles
# diver.switch_to.window(s[1]) #切换至刚打开的界面
# page.ele('xpath://*[@id="sortBarWrap_right"]/div/div/div[8]/div/button[2]/i').click()
#sortBarWrap_right > div > div > div.next-pagination.next-small.next-simple.next-no-border > div > button.next-btn.next-small.next-btn-normal.next-pagination-item.next-next
# page.scroll.down(4200)
# for i in range(10):
#     page.ele("#sortBarWrap_right > div > div > div.next-pagination.next-small.next-simple.next-no-border > div > button.next-btn.next-small.next-btn-normal.next-pagination-item.next-next").click()
#     page.scroll.down(4200)
#     # page.execute_script("window.scrollTo(0,4200)")
#     page.ele('xpath://*[@id="sortBarWrap_right"]/div/div/div[8]/div/button[2]/i').click()
#     if not page_bnt:
#         print('这是最后一页了')
#         break
#     try:
#         page_bnt.click()
#         time.sleep(3)
#     except Exception as e:
#         print(e)
#         page_bnt.click("js")
time.sleep(3)
page.quit()

'''20261015
drissionpage页面自动登录点击脚本'''
from DrissionPage import ChromiumPage as uc
from DrissionPage.common import By
import time
import re
import json
import hashlib
# opt = Options()
# opt.add_experimental_option("detach", True)
#创建浏览器对象，设置超时/重试
page= uc()
page.get("https://www.taobao.com/")
# //*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]
logined=page.ele('css:#J_SiteNavLogin > div.site-nav-menu-hd > div > a')
print(logined.text)
if logined.text=='亲，请登录':
    print('未登录，执行登录操作')
    page.ele('css:#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h').click()
    id_dx = page.ele('xpath://*[@id="fm-login-id"]').clear()
    id_dx.input("15286524744")
    page.ele("#fm-login-password").input("qlok996")
    page.ele('css:#login-form > div.fm-btn > button').click()
    page.ele('css:.login-dialog-footer button.dialog-btn-ok').click()
    page.ele('css:#q').input("图书")
    page.listen.start('https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/')
    page.ele('css:#J_TSearchForm > div.search-button > button').click()
    res = page.listen.wait(timeout=10).response
    print("本次搜索产生的接口：", res.body)
else:
    print('账号已登陆，直接搜索')
    page.ele('css:#q').input("图书")
    page.listen.start('https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/')
    page.ele('css:#J_TSearchForm > div.search-button > button').click()
    res = page.listen.wait(timeout=10).response
    print("本次搜索产生的接口：", res.body)
    # ele=page.ele('css:#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')
    # if ele.text=='亲，请登录':
    #     print('未登录，执行登录操作')
    #     ele.click()
    #     id_dx = page.ele('xpath://*[@id="fm-login-id"]').clear()
    #     id_dx.input("15286524744")
    #     page.ele("#fm-login-password").input("qlok996")
    #     page.ele('css:#login-form > div.fm-btn > button').click()
    #     page.ele('css:.login-dialog-footer button.dialog-btn-ok').click()
    #     login()

# login_ele = page.ele('#J_SiteNavLogin a:contains("亲，请登录")', timeout=3)
# print(login_ele)
# ele=page.ele('xpath://*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
# print(ele.text)
#J_SiteNavLogin
#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h
# cookie=page.cookies()
# print(cookie)
# # page.ele('xpath://*[@id="q"]').input('内裤')
# # page.ele('xpath://*[@id="J_TSearchForm"]/div[2]/button').click()
# ele=page.ele('xpath://*[@id="fm-login-id"]').clear()
# ele.input("15286524744")
# page.ele("#fm-login-password").input("qlok996")
# # page.ele('xpath://*[@id="fm-login-id"]').input('15286524744')
# # page.ele('xpath://*[@id="fm-login-password"]').input('qlok996')
# page.ele('xpath://*[@id="login-form"]/div[7]/button').click()
# page.ele('xpath:/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
# #直接在内容后面加回车
# page.listen.start('https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0')
# page.ele('xpath://*[@id="q"]').input("图书")
# page.ele('xpath://*[@id="J_Search"]/form/button').click()
# page.ele('css:#sortBarWrap_right > div > div > div.next-pagination.next-small.next-simple.next-no-border > div > button.next-btn.next-small.next-btn-normal.next-pagination-item.next-next').click()
# page.listen.start('https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.7.4&appKey=12574478&t=1791914125034&sign=beb1c455a4c5f3f20097465245bf3d12&api=mtop.relationrecommend.wirelessrecommend.recommend&v=2.0&timeout=10000&type=originaljson&dataType=jsonp&bx-ua=234')
# res=page.listen.wait().response
# data=res.body
# print(data)
# # page.quit()
#
# #J_SiteNavLogin > div.site-nav-menu-hd > div > a
