
import time
import pandas as pd
def login(u,p):
    if u=='jile' and p==123:
       time.sleep(2)
       print('成功')
def count_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        print(f'程序运行了{end-start}秒')
        return res
    return wrapper
res=count_time(login)
res('jile',123)

#装饰器调用原函数并为原函数增加拓展功能
from qlok import *
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name="原始数据")
lt=df['年龄'].iloc[:].tolist()
print(f'{modle1.avg(lt):.2f}')


def outer(func):
    def wrapper(*args,**kwargs):
        st=time.time()
        rels=func(*args,**kwargs)
        et=time.time()
        print(f"游戏运行了{et-st}秒")
        return rels
    return wrapper
@outer
def wzry(group,s):
    print(f'你选择了{group}方')
    print(f'敌军还有{s}秒到达战场')
    time.sleep(s)
    print(f'全军出击')
wzry('红色',5)


# def rcdtime():
#     st=time.time()
#     wzry('红色',5)
#     et=time.time()
#     print(f"游戏运行了{et-st}秒")
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         st=time.time()
#         rels=func(*args,**kwargs)
#         et=time.time()
#         print(f"游戏运行了{et-st}秒")
#         return rels
#     return wrapper

def count_t(func):
    def wrapper(*args,**kwargs):
        st=time.time()
        red=func(*args,**kwargs)
        et=time.time()
        print(f'程序运行了{et-st}秒')
        return red
    return wrapper

@count_t
def procline(tol):
    tl=tol
    qian = "\033[38;2;72;209;204m"
    hou= "\033[38;2;238;238;238m"
    rset="\033[0m"
    f_bg='\u2588'
    e_bg='\u2591'
    for i in range(tol+1):
        pt=i/tl*100
        br=qian+f_bg+f_bg*i+rset+hou+e_bg*(tl-i)+rset
        print(f'\r加载中：{br}{pt:.2f}%',end='')
        time.sleep(0.05)
    print()
procline(100)