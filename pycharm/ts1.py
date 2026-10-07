import random

C语言中文="www.baidu.com"  #可以使用中文作为变量函数名
print(C语言中文)

a=1
b=2
c=3
total=a+\
      b+\
      c
print(total)


print(12+5)
print(12-5)
print(12*5)
print(12/5)
print(12%5) #2
print(12//5) #2
print(9.0+2.0)

def avg(nums):
    return sum(nums)/len(nums)
print(avg([3,4,5,6]))

print(round(3.1518,3))

s1="你好！"
s2="我久违的朋友！"
print(s1+s2)
s3=50
print(str(s3)+s2)

age=21
sexy="男"
print("小明性别：%s,年龄：%s岁"%(age,sexy))

#浮点数格式化：%f/%.2f
high=173.2
print("小明身高为：%fcm"%high)
print("小明的身高为：%.2fcm"%high)
rate=0.30
print(f"利率为：{rate:.2f}‰")
print("活期利率为：%.2f%%"%rate)
print("活期利率为：",rate,"%")
r=0.6
print(f"利率为：{r:.2f}%")

age=21.6
print("小红今年%d岁"%age)
name='小明'
print("%s的年纪为%d岁"%(name,age))
con=f"{name}的年龄为{age}岁！"
print(con)

name,age='xiaoming',30.1
print("{}的年纪为{}岁".format(name,age))

sr='hello'
print(sr.count('l'))
print(sr.index('l'))  #索引位
print(sr[sr.index('l'):])
print(sr[1:3]) #不包含后边界3
print(sr[-3])
print(len(sr))

sr1="----江山如画---   "
print(sr1.lstrip(" -"))
print(zip(sr1.split('-',1)))



sr2="hooohhooohhhhsdskoo"
print(sr2.split("oo",2))

#列表的操作方法

'''
添加元素3种方式：
1.append 末尾添加一个元素元素
2.extend 末尾添加多个元素,多个元素必须要用[]包裹起来
3.insert（0，1） 在指定索引位置添加元素 0是索引位置从0开始，1是插入元素内容
删除列表2种方法
按索引删除
1.del()
del course[0] 
也可以范围删除；区间左闭右开
del course[1:3] 意为删除索引位1，2的元素，不包含3（右开）
2.pop()
list.pop(索引位)
按索引位置删除对应元素
list.pop()默认删除最后一个元素
2.按元素内容
remove方法
list.remove('元素内容名称如：专英')
3.清空列表
clear(）
list.clear()
'''
#例子
course=["高数","解析几何","线代","数分"]
course.append('拓扑')
print(course)
course.extend(['传体','专英','统计学'])
print(course)
course.insert(1,'项目管理')
print(course)

del course[0]  #索引0代表开始位置，即删除第一个元素
print(course)
del course[1:3]
print(course)
course.pop(0)
print(course)
course.pop(2)
print(course)
course.pop()  # 默认删除最后一位
print(course)
course.remove('专英')
print(course)
course.clear()
course.extend(['项目管理', '数分', '拓扑', '传体', '专英', '统计学'])
print(course)
course.append('线代')
print(course)
c1=random.choice(course)
print(random.choice(course))

def tj(x):
    if x=='项目管理':
        return f'这是小明的课程：{x}'
    elif x=='数分':
        return f'这是小王的课程：{x}'
    elif x == '拓扑':
        return f'这是小花的课程：{x}'
    elif x == '传体':
        return f'这是小咯的课程：{x}'
    elif x == '专英':
        return f'这是小美的课程：{x}'
    elif x == '统计学':
        return f'这是小流的课程：{x}'
    else:
        return f"暂无人选修的课程：{x}"
c=['项目管理', '数分', '拓扑', '传体', '专英', '统计学']
c.append('高数')
re=list(map(tj,c)) #map函数将c里的元素一次传递给tj处理后输出结果；
print(*re,sep='\n') #*解包列表 seq定义分隔符

a=['标','准','财','务','大','数','据']
print(a[5])
print(a[-1])
print(a[5:7])
a[4]='小'
print(a)
print(a[:3:3])  #c从索引0开始，结束位为3，但不包括3，最后一个数字表示步长：相隔步长-1取数，相隔2，步长为3以此类推
print(max(a))
for x in a:
    code=ord(x)   #ord（）函数可以比较
    print(f"{x}的unicode为：{code}")
print(a.sort(key=ord,reverse=False))  #key直接传函数，不能是执行结果。reverse=F为升序T为降序
print(a.sort(key=None,reverse=False))
b=sorted(a,reverse=True)
print(a)

b=['5','8','2','4','3','1']
print(sorted(b,key=int,reverse=True))
b1=b.sort(key=ord,reverse=True)
print(b)
print(b.pop(0))
print(b)
b.remove('5')
b[1:3]=10,8
print(b)

list1=['企业管理部','财务部','营销部','采购部','仓储部','生产部','人力资源部']
list2=['浅丹','赵小样','高傲','易小川','程度','宽宽']
print(list1,list2)
print(list1[0])
print(list1[2])
print(list1[0:3])  #前三个，不包含后边界3
list1[1]='财务管理部'
print(list1)
list2.append('李小新')
print(list2)
list2.insert(1,'铁蛋')
print(list2)
list2.pop(1)
print(list2)
list2.remove('宽宽')
print(list2)
list2.insert(1,'宽宽')
print(list2)
del list2[1]
print(list2)

sl=[1000,12200,900,850,1100,1500]
print(max(sl))
print(min(sl))
print(sum(sl))
print(f"{sum(sl)/len(sl):.2f}")
print(sorted(sl,key=int,reverse=True))
#sl.sort() 默认升序排列
#sl.sort(reverse=Ture)  降序排列
print(sorted(sl,key=int,reverse=True))
print(sorted(sl,key=int,reverse=False))

name=('资产负债表','利润表','现金流量表')
name1=(3,)  #只有一个元素时要在末尾加上逗号
cont=('亚洲','欧洲','非洲','北美洲','南美洲','南极洲','大洋洲')
print(cont[5])
print(cont[-2])
print(cont[-3:])
print(cont[:-3])
print(cont[1:3])

tupl=(1,2)
t2=(3,4)
print(3 in t2)
print(tupl+t2)
print(("0",)*3)
print(id(tupl))
tupl+=(3,)
print(id(tupl))
print(tupl)
print(name.count('资产负债表'))
print(len(t2))
print(tuple([1,2,3,5,7]))

tel={'娜扎':12345678,'孙悟空':12345679,'东海龙王':12345670}
print(tel['娜扎'])
info={10000:{'name':'娜扎','sex':'男','tel':12345678},\
      10001:{'name':'孙悟空','sex':'男','tel':12345679},\
      10002:{'name':'东海龙王','sex':'男','tel':12345670}}
print(info[10002])  #字典只能单个键查找
print(info.get(10002))
print(tel.get('孙悟空'))
print(tel.get('红孩儿'))
#访问所有值
print(tel.values()) #结果为列表；需要用刀FOR循环取值
for v in tel.values():
    print(v)
print(tel.keys())  #结果为列表；需要用刀FOR循环取值
for k in tel.keys():
    print(k)
#访问所有键值对 item()
print(tel.items())
for k,v in tel.items():
    print(k,':',v)

tel['娜扎']=12345677  #直接修改值；python不支持键的修改，修改只能删除旧的重新添加键值对
print(tel)
tel['红孩儿']=12345675
tel['红孩儿','lisan']=12345675,1245451
tel.pop(('红孩儿','lisan'))
print(tel)
tel.update({'李三':12345671})
tel.update({'zhangsan':55552})
print(tel)
tel.pop('zhangsan')
print(tel)

keys=[10000,10001,10002]
res=[info.get(k) for k in keys]
re=(keys+res)
print(re)
l1=(re[:3])
l2=(re[3:])
l3=[f"{l1}:{l2}" for l1,l2 in zip(l1,l2)]
l4="\n".join(l3)
print(l4)


a=[1,2,3]
b=['x','y']
d=dict(zip(a,b)) #长度不一样的列表只会转换对应的位置，3就会被丢弃
print(d)
c=(a+b)
d=(c[:3])
f=(d[:3])
g=[f"{w}:{c}" for w,c in zip(d,f)]
h="\n".join(g)
print(h)

#并行遍历
names = ["张三","李四"]
ages = [18,20]
for name,age in zip(names,ages):
    print(name,age)

#元组tuple是不可更改类型
dex=['纳斯达克100','纳斯达克综合指数','标普500指数','道琼斯指数']
pr=[11665.37,11484.69,3435.56,28210.82]
res=[f"{d}:{p}"for d,p in zip(dex,pr)]
print(res)  #列表
res2=tuple(res)  #元组
print(res2)
print(res2[2])
res1=dict(zip(dex,pr))  #字典取值用GET （）字典
print(f'标普500指数：',res1.get('标普500指数'))
print(res1)
print(res)
t_dex=tuple(dex)
t_pr=tuple(pr)
print(t_dex)
print(t_pr)

print(res1.get('纳斯达克100'))
#字典的key和value一级item都需要for循环查看
for k in res1.keys():
    print(k)
for v in res1.values():
    print(v)
for k,v in res1.items():
    print(k,':',v)
res1.update({'纳斯达克100':11665.38}) #
#字典增加元素
res1['上证指数']=15822.39
print(res1)
res1.pop('上证指数')
print(res1)
#集合
#集合中的元素都是唯一的
con=set('heojsodajikhflol')
print(sorted(con)) #默认升序
print(sorted(con,reverse=True))
bas=set()
print(bas)
print(type(bas))

set1={1,2,3,4,5,4,2,36,6}
print(set1)  #原始为无序
print(type(set1))
print(len(set1))
for i in set1:
    print(i)
print(6 in set1)
#集合的添加
#add\update
set1.add(7)
print(set1)
set1.update({8,9})
print(set1)
#remove只能删除一个，多个会报错
#set1.remove(7,8,9)
#可以使用循环来删除
del_list=[7,8,9]
for i in del_list:
    if i in set1:  #判断是否存在，不存在会报错
       set1.remove(i)
print(set1)
#discard
set1.discard(36) #用法和remove一样，都是删除元素
print(set1)
set1.discard(100) #discard不存在不会报错
print(set1)
#set1.pop(3) ##报错，集合没有元素下标
print(set1)

#访问集合直接用for循环
#添加用ADD和UPDATE
#删除用remove和discard和pop(不支持传参，默认删除最小数字，非数字随机删除)
#集合的运算
con={"数学","语文","英语","体育"}
all={"数学","语文","英语","体育","物理","历史"}
#交集 &
print(all&con)
#并集
print(all|con)
#对称补集
print(all^con)
#超集
print(all>con)
print(all==con)
print(all<con)
print('python' in con)
print('python' in all)

num={1,2,3,7,6,90}
print(max(num))
print(min(num))
print(len(num))
num.add(6)
print(num)
num.update({8,80})
dl=[8,80]
for i in dl:
    if i in num:
        num.discard(i)
print(sorted(num))
num.update({33,35})
num.add('test')
num1={i for i in num if type(i) in (int,float)}
print(num1)
print(num)
print(sum(num1))


#基金分析
f400015={"亿纬锂能","宁德时代","比亚迪","三花智控","恩捷股份","赣锋锂业","汇川技术",\
         "先导智能","宏发股份","国轩高科","天齐锂业","格林美","新宙邦","璞泰来","杉杉股份"}
f501057={"宁德时代","比亚迪","亿纬锂能","赣锋锂业","汇川技术",\
         "三花智控","华友钴业","恩捷股份","洛阳钼业","先导智能","中航光电","国轩高科","欣旺达","天齐锂业","格林美"}
print(len(f501057))
print(len(f400015))
#对比两只基金前十五持仓中哪些股票是相同的
#转换成求两个集合的交集
print(f400015&f501057)
#对比两只基金前十五持仓中哪些股票是不相同的
print(f400015^f501057) #对此补集
r1=set(sorted(f400015^f501057))
print(r1)
print(f400015-f501057)
print(f501057-f400015)
r2=set(sorted(f400015-f501057))
r3=set(sorted(f501057-f400015))
r4=r2|r3
print(r4)
if (r4 == r1) == True:
    print("对称补集等于两个集合互相求差的后的并集")
else:
    print("对称补集是单独计算的！")
#对比两只基金前十五持仓中一共有多少只不同的股票
#并集
print(len(f400015|f501057))

print('❤')
print('💞❤💞')
print('💞❤💞')
print('💞❤💞')
print('❤')


#多个变量一起赋值
a,b,c=1,2,3
print(f'{a+b+c}')
# f='北京'
# s='河南'
# t='河北'
f,s,t='北京','河南','河北'
print(f,s,t)
o,tw,tr,fr=63,36,22,29
o1,tw1,tr1,fr1=54,60,40,30
sum=o+o1
print(sum)
data=(tw1-tw)/tw
print(f"{data:.2f}")
if o>o1:
    print("21第一季度下降")
elif o==o1:
    print("2021第一季度持平")
else:
    print("2021第一季度下降")

pa,pb,ow=100,400,200
print(pa>pb and pb>ow)
print(pa>pb or pb>ow)

op='o为奇数'if o%2 == 1 else "o是偶数"
print(op)

a='尺子'
b=['钢笔','尺子','橡皮','铅笔']
c="a在b中" if a in b else"a不在b中" #直接写判断结果满足if 打印左边，else打印右边
print(c)
##三目运算

c,d=23,23
y="c,d相同"if c is d else "c,d不相同"
print(y)

#lambda
#lambda [参数列表]：表达式
#1,无参数
f=lambda: 99
print(f())
#2单个参数

