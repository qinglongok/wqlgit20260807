import requests as rq
import pandas as pd
import re
import datetime
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from bs4 import BeautifulSoup
url='https://www.weather.com.cn/weather1d/101010100.shtml'
resp=rq.get(url)
resp.encoding='utf-8'
print(resp.text)
city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd=re.findall('<span class="wd">(.*?)</span>',resp.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)
#print(city)
#print(weather)
#print(wd)
#print(zs)


list=[]
for a,b,c,d in zip(city,weather,wd,zs):
    list.append([a,b,c,d])
    print(list)
for item in list:
    print(item)
dict=[(a,b,c,d) for a,b,c,d in zip(city,weather,wd,zs)]
print(dict)
col=list[0]
table_title=header=f'{datetime.datetime.now().strftime("%Y-%m-%d")}天气数据表'
df = pd.DataFrame(list,columns=col)
print(len(df))  ##爬去到的数据的条数
path=r"D:\pycharm\test.xlsx"
try:
  with pd.ExcelWriter(path, engine='openpyxl', mode='a',if_sheet_exists="replace") as writer:
          df.to_excel(writer, sheet_name='爬取结果', index=False,startcol=1)
          ws=writer.sheets["爬取结果"]
          ws.merge_cells(f"A1:{get_column_letter(5)}1")
          ws.cell(row=1,column=1,value = table_title).alignment=Alignment(horizontal="center", vertical="center")
          ws.cell(row=2,column=1,value='序号')
          strow=3
          endrow=strow+len(df)-2 #按常理减一就行，但是爬取内容的第一条是列名不是数据，故要减去列名这一行
          for row in range(strow,endrow+1):
              sq=row-strow+1
              ws.cell(row=row, column=1, value=sq).alignment=Alignment(horizontal="center", vertical="center")
  print(f"✅ 数据爬取完成，已保存到 {path}.爬取结果")
except PermissionError:
    print(f'❌ 错误：文件 {path} 正在被使用，请关闭 Excel 文件后重试。')


from numpy.matlib import rand

for i in range(1,10):  #控制输出内容的行数
   for j in range(1,i+1): #控制输出多少列
      # print(j,'*',i,'=',i*j,end='\t')
       print(f"{j}*{i}={i*j}",end='\t')
   print('')

import random
#arr=input('请输入需要排序的数字，用空格分隔：').split()
#arr1=list(map(int,arr))
arr=random.sample(range(1,101),5)
print(type(arr))
arr1=arr
print(arr1)
n=len(arr1)
for i in range(0,n):
       for j in range(0,n-i-1):
         if arr1[j]>arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
           # temp=arr1[j]
           # arr1[j]=arr1[j+1]
           # arr1[j+1]=temp
print('排序结果为：',arr1)
rs=arr1
zh=int("".join(map(str,rs)))
print('排序结果为：',zh)
random.shuffle(arr1)
zh=int("".join(map(str,arr1)))
print('排序结果为：',zh)

import random
num1={'小红':98,'李雷':85,'韩梅梅':95,'马冬梅':93}
re=list(num1.keys())
print(random.choice(re))
print('I\'m OK!')
print("x\0y")


grade = [98,96,95]
res = map(int, grade)
print(res)  # <map object at 0xxx>，迭代器不能直接看内容

# 转列表查看结果
res_list = list(res)
print(res_list) # ['98', '96', '95']

# 引号、换行、Tab、反斜杠一起用
s = "姓名\t年龄\n小明\t18\nHe said:\"I\\'m 18\""
print(s)


# 普通字符串 \会报错
path = "C:\new\test.txt"

# 原始字符串，所有\原样输出
path = r"C:\new\test.txt"
print(path) # C:\new\test.txt


def double(x):
    return x **2

num = [1, 2, 3, 4]
result = list(map(double, num))
print(result)


def hello():
    print("hello")
hello()

from tkinter import messagebox as msg

from qlok import modle1

a=70
if a > 60 :
    # msg.showinfo('提示信息!','人数合规，允许进入！')
    print(f'这个班超过60人，人数为:{a}')
print(f'判断段语句执行结束！')

b=200  #int(input("请输入你的零花钱金额："))
if b > 100 :
    print(f'超过100元！')
else:
    print(f'未超过一百元')

pm=25
gk=0
if pm<=20:
    print(f'成绩排名在前20')
    if gk>0:
        print(f'存在挂科，不可参选！')
    else:
        print(f'没有科目不及格！且成绩排名在前20，可以参选。')
else:
    print(f'成绩不合格不可参选')

for i in range(1,11):
    print(i,end=' ') #不换行输出
print()

for i in range(1,10): #控制行数
    for j in range(1,i+1): #控制每行列数
        print(f'{j}*{i}={i*j}',end='\t')
    print()

#打印0-50的所有奇数
for i in range(51):
    if i%2!=0:
        print(i)

#乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}',end='\t')
    print()

#while循环
num=1
sum=0
while num<=100:
    sum += num  #先求和在自增，不然计算的就是2-101的和
    num+=1
print(f"和为{sum}")

def dg(形参):
    #设置出口
    if 形参==1:
        return 1
    re=形参+dg(形参-1)
    return re
print(dg(100))
import functools
print(functools.reduce(lambda x,y:x+y,range(1,101))) #高级函数的运用 计算-100的和

#输出10以内的偶数 while
num=0
while num<=10:
    if num%2==0:
        print(num)
    num+=1

#倒计时
import time
import random
from datetime import date
import datetime
print(time.ctime())
tm=datetime.date(2026,8,11).strftime('%Y/%m/%d')
t1=date(2026,8,11)
print(t1)
print(tm)
now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cnt=1
while cnt!=0:
    print(f'{cnt}秒')
    time.sleep(1)
    cnt-=1
print(f'计时结束！当前时间：{now}')

fct=0
while fct<70000:
    cgl=70000-fct
    print(f'食物总量：{fct},食物不够,还需采购{cgl}份！')
    fct+=10000
print(f'食物总量：{fct},满足需求，采购完成')

# c = 0
# a = random.randint(1, 100)
# while True:
#     b=int(input(f'请输入你猜的数字：'))
#     if not isinstance(b,int) and b<0 and b>100:
#          print(f'请输入1-100的整数')
#     c+=1
#     if b==a:
#         print(f'恭喜你猜对了！答案为：{a},你一共猜了{c}次')
#         break
#     elif b<a:
#         print(f'小了')
#     else:
#         print(f'大了')

num=0
while num<10:
    num+=1
    print(num)

for i in range(1,6):
    if i not in [2,3,4,5]:
        continue  #跳过往后的逻辑代码
    print(i)

def dg1(x):
    if x==1:
        return 1
    res=x+dg1(x-1)
    return res
dg1(365)

x=(i for i in range(1,6))
print(list(x))
print(list(x))
#--all--【】只有括号里的函数
from qlok import *
modle2.maopao([0,4,5,7,3])


#@property 静态属性 ：把类的函数属性封装成类似于数据属性，调用时直接用 对象.函数名 （！必须不带括号）

class yoy():
    @property
    def m(self):
        print(f'这是一个静态属性')
dx=yoy()
dx.m

from openpyxl.styles.builtins import percent

a=10000000
arra=list(range(1,a+1))
arrb=list(range(1,a+1))
res=0
for i in range(len(arra)):
    res+=arra[i]*arrb[i]
print(res)


import  numpy as np
n=10000000
ar=np.arange(1,n+1,dtype=object)
br=np.arange(1,n+1,dtype=object)
res=np.dot(ar,br)
print(res)

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
    '8':['t''u''v'],
    '9':['w','x','y','z'],
}
    letter=[key_map[d] for d in digt]
    print(letter)
    cob=list(itertools.product(*letter))
    comb=["".join(cmb) for cmb in cob]
    return comb
win=tk.Tk()
win.title(f'CACL')
win.geometry('300x400')
win.configure(background='pink')
win.mainloop()




import tkinter as tk
from tkinter import Button


class NineGrid():
    def __init__(self, root):
        self.root = root
        self.root.title("九宫格按钮")
        self.root.geometry("400x400")

        # 创建九宫格按钮
        self.create_grid()

    def create_grid(self):
        # 使用 grid 布局创建 3x3 按钮
        buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                num = row * 3 + col + 1
                btn = Button(
                    self.root,
                    text=f"按钮 {num}",
                    font=("Arial", 14),
                    width=4,
                    height=3,
                    command=lambda n=num: self.button_click(n)
                )
                btn.grid(row=row, column=col, ipadx=20, ipady=20, sticky="ns")
                row_buttons.append(btn)
            buttons.append(row_buttons)

        # 设置网格权重，使按钮随窗口缩放
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, num):
        print(f"点击了按钮 {num}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NineGrid(root)
    root.mainloop()

import re
print('''
人力部经理是：胡然
财务部经理是：钱丹
营销部经理是：周进
''')
print('''
钱丹是财务部经理，
员工编号1006，
性别“女”。
''')

a='我们是冠军'
b='hello to my licent'
print(f'{a:=^40}')
print(a+' '+b)

from datetime import datetime
try:
    while True:
        name ='钱丹' #input(f'请输入姓名：')
        if name=='钱丹':
            print(f'姓名验证正确')
            while True:
                id = '810110197605066606' #input(f'请输入身份证号：')
                if len(id)==18:
                    birth=id[6:14]
                    try:
                        d_day=datetime.strptime(birth,'%Y%m%d')
                        rs=datetime.strftime(d_day,'%Y年%m月%d日')
                        print(f'{name}的出生日期是：{rs}')
                        break
                    except ValueError as e:
                        print(f'{birth}不是合法日期')
                else:
                    print('id长度错误')
            break
        else:
            print('姓名输入错误，请重新输入！')
except KeyboardInterrupt as e:
    print(e)

# split  分手
# join  复合
mail='5002815@qq.com'
qq=re.findall(r'\d+',mail) #findall 结果为列表<class 'list'>
print(type(qq))
qq1=mail.split('@')[0]  #类似与awk -F'@' '{PRINT $1}'打印用户名
l1=mail.split('@')[1]
l2=[l1,qq1]
em="@".join(l2)
print(em)
print(qq1)
print(*qq)
num1='abc18010898989'
q=num1.count('8')
print(q)

ls=['钱丹','赵晓阳','高敏']
emp1='12'
if emp1 in ls:
    print(f'{emp1}是财务部员工')
else:
    print(f'{emp1}不是财务部员工')


import pandas as pd
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
data=[
    {
        '订单号':'10234450667',
        '单据编号':'40056320',
        '业务日期':'2020/4/1',
        '客户':'北京美迪电器销售有限公司',
        '部门':'营销部',
        '业务员':'张萌',
        '币种':'人民币',
        '金额':265444.00
    },
    {
        '订单号':'10234450125',
        '单据编号':'40040321',
        '业务日期':'2020/5/5',
        '客户':'长沙蒙宁电器销售有限公司',
        '部门':'营销部',
        '业务员':'李妮',
        '币种':'人民币',
        '金额':159570.00
    }
]
data.append({
        '订单号':'10234450889',
        '单据编号':'40058152',
        '业务日期':'2020/8/11',
        '客户':'北京美迪电器销售有限公司',
        '部门':'营销部',
        '业务员':'咕嘎',
        '币种':'人民币',
        '金额':130250.00
})
df=pd.DataFrame(data,index=range(1,len(data)+1))
# df['金额']=pd.to_numeric(df['金额'],errors='coerce').round(2)
path=r"D:\pycharm\test.xlsx"
title=f"{datetime.now().strftime('%Y年%m月%d日')}应收账款数据表"
try:
    with pd.ExcelWriter(path,engine='openpyxl',mode='a',if_sheet_exists='replace') as writer:
        df.to_excel(writer,sheet_name='应收账款数据',index=False,startrow=1)
        ws=writer.sheets['应收账款数据']
        max_col=df.shape[1]
        ws.merge_cells(f"A1:{get_column_letter(max_col)}1")
        ws.cell(row=1,column=1,value=title).alignment=Alignment(horizontal="center",vertical="center")
        ws.cell(row=2,column=1,value='序号')
        strow=3
        edrow=strow+len(df)-1
        for l in range(strow,edrow+1):
            sq=l-strow+1
            ws.cell(row=l,column=1,value=sq).alignment=Alignment(horizontal="center",vertical="center")
        print(f'成功添加到{path}中')
except Exception as e:
    print(e)
