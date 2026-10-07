#创造列表
ls1=[i for i in range(1,11) if i%2!=0]
print(ls1)

from openpyxl import load_workbook
path=r"D:\pycharm\test.xlsx"
wb = load_workbook(path,data_only=True) #data_only：true表示读取最终计算结果 false表示读取原始计算公式
ws=wb["Sheet3"]  #读取工作表中的sheet1(可以修改为sheet2)
lst=[cell.value for cell in ws["B"][1:] if cell.value is not None]
print(lst)
data=[]
header=[cell.value for cell in ws[1] if cell.value is not None]
print(header)
for row in ws.iter_rows(min_row=1,max_col=3,values_only=True):
    data.append(list(row))
print(data)
data.pop(0)
print(data)
print(lst)
lst[1:3]=88,99
print(lst)
lst[3]=88
print(lst)
print(lst.index(88))
tr=88
sy=[i for i,v in enumerate(lst) if v==tr] #找到重复元素的多个索引位置
print(sy)
lst.pop(1)
print(f"年龄明细为：",*lst)
print(f"年龄和wei:",sum(lst)) #统计列表的和
print(f"年龄个数为：{len(lst)}")
lst1=sorted(lst,reverse=True)
print(f"年龄从大到小排列为：",*lst1)
lst.remove(31) #remove列表删除时只会删除第一个
print(lst)
#删除多个使用for循环
dl=[26,29]
for i in dl:
    if i in lst:
        lst.remove(i)
print(lst)
lst.extend(dl)
print(lst)
ml=sorted(lst,reverse=True)
print(ml[:2])

def avg(x):
    if len(x)==0:
        return ("x不合法，请输入合法字段")
    return sum(x)/len(x)
print(f"平均年龄为：{avg(lst):.2f}")
#使用for循环计算
sum=0
cot=0
for i in lst:
    sum+=i
    cot+=1
avg=sum/cot
print(avg)

from openpyxl import load_workbook
path=r"D:\pycharm\test.xlsx"
wb=load_workbook(path,data_only=True)
ws=wb["Sheet3"]
lst1=[cell.value for cell in ws["A"][1:] if cell.value is not None]
print(lst1)
lst2=[]
for row in ws.iter_rows(min_row=2,values_only=True):
    lst2.append((row[1],row[2],row[3]))
print(lst2)

lst3=[f"{item[0]}{item[1]}{item[2]}" for item in lst2]
print(lst3)
dc=dict(zip(lst1,lst3))
print(dc)
for k,v in dc.items():  #遍历字典用item
    print(f"{k}: {v}")

import pandas as pd
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name="Sheet3")
print(df.columns.to_list())
print(df[['姓名','电话']])
l4=list(zip(df['电话'],df['年龄']))
l6=list(df['姓名'])
print(l6)
print(l4)
l5=[f"{item[0]}{item[1]}" for item in l4]
print(l5)

dc1=dict(zip(l6,l5))
print(dc1)
for k,v in dc1.items():
    print(f"{k}: {v}")
print(dc1['刘洋'])
print(dc1.get('刘洋'))
#字典添加update
dc1.update({'姚婷':1392236585630})
dc1['姚大']=1392236585633
dl1=['姚婷','姚大']
for i in dl1:
    if i in dc1:
        del dc1[i]
print(dc1)
print(f"客户数量为：{len(dc1)}")
for k in dc1.keys():
    print(f"{k}")
lx="\n".join(dc1.keys())
print(f"清单为：\n{lx}  ")
zh="\n".join(dc1.values())
print(f"联系电话清单：\n{zh}")
zt=dc1.items()
print('❤'*30)
print(f"姓名及信息清单:")
print('❤'*30)
for k,v in zt:
 print(f"           {k}:{v}")
print(dc1.get('郑浩','此人不存在！'))
print(dc1.get('姚大','此人不存在！'))
ke='姚大'
k=dc1.keys()
if ke in k:
    print(dc1.get(ke))
else:
    print(f"{ke}此人不存在!")

import pandas as pd
data = {'姓名': ['John', 'Alice', 'Bob'],
        '年龄': [25, 30, 35],
        '城市': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
df.to_excel('test2.xlsx')
print(type(df))

import pandas as pd


# import time
# def JinDuTiao(tl=100):
#     '''进度条'''
#     for i in range(tl+1):
#         percent=i/tl*100
#         jd='❤️'* i + '🤎'*(tl-i)
#         print(f'\r进度：{jd}{percent:.2f}%',end='')
#         time.sleep(0.02)
#     print()
#     print('✅welldown')
# JinDuTiao(30)

def  dg(x):
    if x==1:
        return 1
    res=x*dg(x-1)
    return res
print(dg(5))

def dg1(x:int):
    res=1
    for i in range(1,x+1):
        res *= i
    return res
print(len(str(dg1(100))))

def m(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print("输入有误！")
        return -1
    while (n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3
r=m(10)
print(r)




def  hanoi(n,a,b,c):
    if n==1:
        print(f'{a} --> {c}')
    else:
        hanoi(n-1,a,c,b)
        print(f'{a} --> {c}')
        hanoi(n-1,b,a,c)
#n=int(input("请输入层数："))
#hanoi(n,'A','B','C')


f=([1,2,3],'to',22,9.2)
print(type(f))
f[0][0]=99
a,b,c,d='qlok'
print(a)


import time
from docx import Document
try:
    dc=Document(r"C:\Users\qlok\Desktop\观潮.docx")  #docx文件不支持直接OPen
#可以使用
    try:
          # while True:
          #   con=f.readline()
          #   if len(con) == 0:
          #     break
          for line in dc.paragraphs:
              print(line.text)
    except:
        print("error")
except Exception as e:
    print(f"{e}")



a='we are the friend from all over the wolrd'
b=a.find('the') #7返回字符串开头字符所在的下标，
c=a.find('kol')
print(c) #字符串不存在则返回-1
print(b)
na=a.upper()
print(na)
ta=a.title()
print(ta)

sa=a.startswith('th')
print(sa)
ea=a.endswith('rd')
print(ea)
da=a.isalpha()
print(da)
print(list(a.split('the')))
ls=['tom','lily','qlok']
n=''.join(ls)
print(n)
i=0
while i<len(ls):
    print(ls[i])
    i=i+1

import pandas as pd
import random
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name='Sheet4')
ls=df['姓名'].iloc[:].tolist()
random.shuffle(ls)
offices=[[],[],[],[]]  #列表里嵌套
for r in range(4):
    offices[r].append(ls[r])
for p in ls[3:]:
    s=random.randint(0,3)
    offices[s].append(p)
i=1
for office in offices:
    print(f"办公室{i}:{" ".join(office)},共{len(office)}人")
    i=i+1

lst=[i for i in range(2,10,2)]
print(lst)

total=50
oo='c'
kk='e'
for i in range(total+1):
 a=oo*i+kk*(total-i)
 print(f'\r{a}',end='')
 time.sleep(0.001)
print()


# 72,209,204 青色
total = 50
# #4caf50 → R=76 G=175 B=80
green_fg = "\033[38;2;72;209;204m"
op = "\033[35;2;166;63;232m"
# #eeeeee → R=238 G=238 B=238
gray_fg = "\033[38;2;238;238;238m"
reset = "\033[0m"
a='\u2588'  # Unicode字符表
b='\u2591'
for i in range(total + 1):
    bar = green_fg + a*i + reset + gray_fg + b*(total-i) + reset
    pct = i / total * 100
    print(f"\r进度：{bar} {op}{pct:.1f}%{reset}", end="")
    time.sleep(0.005)
print()


lst1=[(i*j) for i in range(2,5)for j in range(5,8)]
print(lst1)

import numpy as np
m=np.array([
    [2,0.5,1],
    [3,4,2],
    [5,1,0.3]
])
re=(np.linalg.det(m))
print(f'{re:.2f}')

dex=['纳斯达克100','纳斯达克综合指数','标普500指数','道琼斯指数']
pr=[11665.37,11484.69,3435.56,28210.82]
dct={dex[i]:pr[i] for i in range(len(dex))}
rs1={k:v for k,v in dct.items() if v>=11500.00}
print(rs1)
print(dct)
print(dct.get('纳斯达克100'))
res=[f"{d}:{p}"for d,p in zip(dex,pr)]
print(res)

import random
def yu():
    '''随机取一个烟名'''
    ls=['中华','玉溪','利群']
    rs=random.choice(ls)
    return rs

def buy():
    return yu()
print(buy())

def cacl(a,b):
    '''
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 参数1+参数2的和
    '''
    sum=a+b
    return sum
print(cacl(20,30))


tal=50 #定义进图条长度

for i in range(tal+1):
    pct=i/tal*100
    br='♥'*i+'🖤'*(tal-i)
    print(f'\r进度：{br}{pct:.2f}%',end='')
    time.sleep(0.005)
print()

for i in range(10):
    print(f'\r{i}',end='')
    time.sleep(0.005)
help(cacl)

def djs(n):
   for i in range(n,0,-1):
        print(f'\r倒计时：{i}秒',end='')
        time.sleep(0.002)
   print('\r结束了')
djs(10)

def djs1(n):
    i=n
    while i>=1:
        print(f'\r倒计时：{i}秒',end='')
        time.sleep(0.005)
        i-=1
    print('\r结束了')
djs1(10)

def test2():
    print('---开始2函数----')
    print('---这是2函数----')
    print('---结束2函数----')
def test1():
    print('---开始1函数----')
    test2()
    print('---结束1函数----')
test1()

def prline():
        print('-'*20)
if __name__=='__main__':
    prline()

def prline2(num):
    i=0
    while i<num:
        prline()
        i+=1
prline2(2)



print('胡然')


