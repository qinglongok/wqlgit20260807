
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
