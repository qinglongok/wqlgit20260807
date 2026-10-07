#h函数
#递归
# 例子 计算1+2+3+。。。+100的和
from functools import reduce

from numpy.testing.print_coercion_tables import print_cancast_table


def  add(x):
     if x == 1:    #终止条件，当
         return 1
     sum=x+add(x-1)
     return sum
rsum=add(10)
print(rsum)
# 计算步骤
# 函数的返回值为：sum=传入变量+add(变量-1)
# 即：
# add(10)=10+add(9)
# add(9)=9+add(8)....
# add(2)=2+add(1)
# add(1)=1

#lambda
#定义一个函数
def a():
    return 20
print(a())
#用lambda表示直接可写成
print((lambda :520)())

def js(a,b):
    return a+b
print(js(10,20))
#用lambda表示直接可写成 也可以实现
print((lambda a,b:a+b)(10,20))

#默认参数
def qh(a,b,c=10):
    return a+b+c
print(qh(10,20))

#lambda
print((lambda a,b,c=10:a+b+c)(10,20))
#可变参数
def hs1(*args):
    return args
r1=hs1(1,2,3)
x1=r1.index(2)
print(x1) #*args 返回结果为元组形式
#元组
a=(1,3)
b=(3,)
c=a+b #元组能加，但不能修改和增加 元组可以使用函数max min count(元素)
print(c)
print(c.count(3))
if ('9' in c) == False:
    print(f'9不在元组内！')
else:
    print('misserror')
def hs2(*args):
    return args
r2=hs2(1,2,3)
print(r2)
print((lambda *args:args)(1,2,3))
#可变关键字参数
#**kwargs
def hs3(**kwargs):
    return kwargs
#字典嵌套输入
print(hs3(
          lisa={'age':35,'sex':'女','tel':15412},
          jack={'age':44,'sex':'男','tel':15455}
         )
     )
#lambda
print((lambda **kwargs:kwargs)(lisa={'age':35,'sex':'女','tel':15412},
          jack={'age':44,'sex':'男','tel':15455}
                              )
      )
#带条件的lambda
def hs4(a,b):
    return a if a>b else b
print(hs4(1,2))
#lambda
print((lambda a,b:a if a>b else b)(1,2))
#lambda排序
ls=[1,12,3,5,8,6] #纯数字列表直接排序
rls=sorted(ls)
print(rls)

ls1=[{'age':35,'sex':'女','tel':15412},
  {'age':44,'sex':'男','tel':15455}]
rls1=sorted(ls1,key=lambda x:x['age'])
print(rls1)

#filter ()；作用：过滤序列中不符合条件的元素 FILTER(筛选逻辑，列表）：\
# 将列表中的每个元素放入筛选逻辑中进行计算，符合逻辑的结果返回出来
#函数写法
ls2=list(range(1,11))
def hs5(x):
    if isinstance(x,(int,float)):
       return x%2==0
rs2=filter(hs5,ls2)
# hs5(ls2) #参数直接传入函数直接报错
print(list(rs2))
#lambda 写法
ls3=[1, 'zhuxian', 3, 4, '中国', 6, 7, 8, 9, 10]
print(list(filter((lambda x:x%2==0 if isinstance(x,(int,float))  else x),ls3)))
print(list(filter(None,ls2)))
print(list(filter(None,ls2)))

##过滤中文字符的函数
import  re
def  has_cz(x):
    '''检查x中是否含义中文，有，True,没有,false'''
    if not isinstance(x,str):
        return False
    return bool(re.search(r'[\u4e00-\u9f5a]',x))
ls3=[1, 'zhuxian', 3, 4, '中国', 6, 7, 8, 9, 10]
l=filter(lambda x: (not isinstance(x,str) or not has_cz(x)),ls3)
#lambda判断为T filter 保留 为F 直接过滤
print(list(l))

#map
#函数形式
def mp(x):
    return x**2
res3=map(mp,range(1,4))
print(list(res3))
#lambda
print(list(map(lambda x:x**2,range(1,4))))
#reduce函数
#语法
# reduce(函数名(a,b),可迭代对象（列表元组）)
# 作用：函数中必须有两个参数，每次函数计算的结果继续和下一序列的元素做累计求和
#属于functools 模块下的 需要导入
#函数形式
import functools
import operator
def red(x,y):
    return x+y
rs1=functools.reduce(red,range(1,4))
print(rs1)

#lambda
print(functools.reduce(lambda x,y:x+y,range(1,4)))


#for循环
sum=0
for i in range(1,6):
    sum+=i
print(sum)

def lol(i):
    if i==1:
        return 1
    sum=i+lol(i-1)
    return sum
lol(5)

print(reduce(lambda a,b:a*b,range(1,5)))


