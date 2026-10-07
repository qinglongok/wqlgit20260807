#类属性和实例属性

class 复仇者联盟(object):
    #类属性
    a='这是一个类属性'
    b='ppoo'
    def 实例方法(self):
        print('打灭霸'        '')
蜘蛛侠=复仇者联盟()
b2幽灵=复仇者联盟()

#用类访问
print(复仇者联盟.a)
#用对象访问 对象.类属性
print(蜘蛛侠.a)
print(b2幽灵.a)
#类属性只能通过类对象修改，不能通过对象修改，使用对象修改只会给对象创建一个实例属性
复仇者联盟.a='这是修改后的类属性'
print(复仇者联盟.a)
#用对象访问 对象.类属性
print(蜘蛛侠.a)
print(b2幽灵.a)
#使用对象修改
蜘蛛侠.a='这是用对象修改的类属性'
print(复仇者联盟.a)
#用对象访问 对象.类属性
print(蜘蛛侠.a)
print(b2幽灵.a)
#类的方法私有属性调用
class lm():
    __wq ='倚天剑'
    @classmethod
    def get_wq(cls):
        return cls.__wq
dx=lm()
print(dx.get_wq()) #对象调用类的私有属性
#静态方法
class Lm1(object):
    @staticmethod #装饰器
    def 静态方法():
        print('这是一个静态方法调用！')
dx1=Lm1()
Lm1.静态方法()
dx1.静态方法()

#静态属性
class lm2(object):
    @property
    def hsm(self):
        print("结果不能带括号执行")
dx3=lm2()
dx3.hsm

#闭包

def fa1(a,b):
    c=1
    def fa2():
        s=a+b+c
        print(f"相加的结果是：{s}")
    return fa2
va=fa1(2,3)
va()

#装饰器
def a1(x):
    def a2(*args,**kwargs):
        print("开始")
        x(*args,**kwargs)
        print("结束")
    return a2
@a1
def a3():
    print('qlok')
a3()
@a1
def a4(va):
    print(f'{va} is qlok')
a4('lisa')
@a1
def a5(va2):
    print(f'{va2} is 固定传参！')
a5(60)
#传键值对参数
@a1
def a6(**kwargs):
    print('清单：')
    for k,v in kwargs.items():
      print(f'{k[0:]}')
      print(f'{k} is {v}')
a6(k1='qlok',xingming='juju',age=58)

#lambda 参数列表：表达式
#他是一个函数，使用时需要被调用：变量名（）

res=[lambda :i for i in range(1,4)]
#print(res[0])  #未调用
print(res[0]()) #3
print(res[1]()) #3
print(res[2]()) #3  结果都是3
res=[lambda i=i :i for i in range(1,4)]
print(res[0]()) #1
print(res[1]()) #2
print(res[2]()) #3

f=lambda: 42
print(f)  #打印内存地址
print(f()) #打印结果42

re1=(lambda a:a**2)
print(re1(5))
re2=(lambda a,b,c:a+b)
print(re2(2,3,3))  #lambda定义几个参数，调用就需要传几个
f=[lambda : x for x in range(1,4)]
#print(f[0]) #报错
print(f[0]())  #闭包陷阱，只返回最后一个值
print(f[1]())
print(f[2]())

import dis
f=lambda a,b:a+b
dis.dis(f)

a=1
f1=lambda a:a
f2=lambda a=a: a
print("f1 的字节码：")
dis.dis(f1)
print("f2 的字节码：")
dis.dis(f2)

f3=[lambda i: i for i in range(1,4)]
#lambda i: i 没有默认值，调用是传入啥显示啥
# def lambda(agre)
#    expression
#    return  expression
# lambda 参数：表达式
# lambda i=i: i 有默认值，调用时没有传入值就显示默认值

#函数
#语法
# 定义：
# 关键字：def  函数名（形参：接收函数调用实参时传入的参数）
#     代码1
#     代码2
# 调用函数：
# 函数名（实参)
def name(a,b):
    '''这是一个
    加法函数'''
    i=a+b
    print(i)
name(1,2)

#help(name) 说明文档调用方法

#位置参数:参数位置必须对应
def  abc(n,g,s):
    print( f"你的姓名是{n},性别是{g},年龄是{s}")
abc('lisa',20,'男')
#关键字参数：形式 k=v，都是kv形式时可以打乱位置
#如果存在位置参数时必须按照顺序填写
abc(s='男',n='lisa',g=20)
#abc(20,'lisa',n='男') # 报错


#修改全局变量需要用global
a=2
def xg():
    global a
    a=3
    print(a)
xg()

#函数（递归）
def  函数名(形参):
    if 形参 == 10:
       return 10
    结果=形参+函数名(形参+1)  #函数内部调用自己必须要留出口
    return 结果
变量=函数名(2)
print(变量)

#先用CLASS定义类，命名必须为驼峰行 TsssMss
class Tm(): #定义类（对象需要做的事情的最终目的名称）
     name = "" # 添加类属性(类变量），如果需要的话
     age=''
     #定义实例方法中的调用参数
     def __init__(self,name,age): #用魔法方法初始化对象（self)
         self.name= name
         self.age= age
    #定义实例方法（变量要实现的事情)
     def method(self):
         print(f'姓名：{self.name},年龄：{self.age}')
dx=Tm('lisa',20) #对象实例化，确定用对象属性要干嘛（做tm这件事（装冰箱））
dx.method()
#面包
class  Bread():
    #首先定义类属性（没有就可以不写）
    #定义构造函数（初始化方法）：初始化对象属性，
    def __init__(self):
        #定义烘培时间
       self.sj=0 #初始状态为0
        # 定义烘培状态
       self.sta='生的'
        # 定义调料清单 清单都用列表形式
       self.tl=[]
    #定义实例方法，定义如何使用属性的逻辑
    def hksj(self,sj):
        self.sj += sj
        if 0 < self.sj < 3:
            self.sta='生的'
        elif 3 <= self.sj < 5:
            self.sta='半生不熟'
        elif 5 <= self.sj < 8:
            self.sta='熟了'
        else:
            self.sta='糊了'
    def tjtl(self,tl):
        self.tl.extend(tl)
    def __str__(self): #返回函数字符内容
        return (f"烘焙时间{self.sj}分钟，面包状态为{self.sta}，添加的调料有:{'、'.join(self.tl)}")
mb=Bread()
mb.hksj(3)
mb.tjtl(['鸡蛋','面粉','水'])
print(mb)
mb.hksj(4)
mb.tjtl(['蛋液','草莓'])
print(mb)
#点餐
a='欢迎使用点餐系统'
print("="*40)
print(fr'{ "\t"*3}【{a}】')
print("="*40)

#单继承
class Paf(object):
    def __init__(self):
        self.age=30
    def mtd(self):
        print(f'这是PAF类的实例方法，打印{self.age}')
class Som(Paf):  #som类没有实例方法但通过关联paf（父类），
    pass
nl=Som()  #对象属于som类
nl.mtd()  #可以继承他所在类继承的父类的方法（mtd)
#多继承，一个类可以关连多个父类，可同时继承多个父类的实例方法，
class pf(object):
    def __init__(self):
        self.tc='唱歌'
    def mtd(self):
        print(f'这位父类可继承{self.tc}技能。')
class pf1(object):
    def __init__(self):
        self.tc = '跳舞'
    def mtd(self):
        print(f'这位父类可继承{self.tc}技能。')
#关联父类
class pf2(pf1,pf):
    pass
dx=pf2()
dx.mtd()  #这位父类可继承唱歌技能 默认技能第一个pf 的
dx.mtd()  #这位父类可继承唱歌技能。结果依然是pf


class pf(object):
    def __init__(self):
        self.tc='唱歌'
    def mtd(self):
        print(f'这位父类可继承{self.tc}技能。')
class pf1(pf):
    def __init__(self):
        self.tc = '跳舞'
    def mtd(self):
        print(f'这位父类可继承{self.tc}技能。')
#关联父类
class pf2(pf1):
    pass
dx=pf2()
dx.mtd()
print(pf2.__mro__) #打印继承链


class pf(object):
    def __init__(self):
        self.tc='唱歌'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
class pf1(object):
    def __init__(self):
        self.tc = '跳舞'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
#关联父类
class pf2(pf1,pf):
    def __init__(self):
        self.tc='下棋'
    def mtd(self):
        print(f'自己的技能是{self.tc}')
    def dy_rest(self,pfc):   #封装成一个函数
        '''调用父类并恢复自身属性'''
        pfc.__init__(self)
        pfc.mtd(self)
        self.__init__()  #将自身属性做初始化恢复自身属性
        print(f'自己的技能是{self.tc}')
    def pf_m(self):
        self.dy_rest(pf) #调用第一个父类
    def pf1_m(self):
        self.dy_rest(pf1) #调用第二个父类
    # def pf_m(self):      #将父类的属性值添加到自身属性里（多个时每个独立添加）
    #     pf.__init__(self)
    #     pf.mtd(self)
    #     self.__init__()    #将自身属性做初始化
    #     print(f'自己的技能是{self.tc}')
    # def pf1_m(self):
    #     pf1.__init__(self)
    #     pf1.mtd(self)
    #     self.__init__()
    #     print(f'自己的技能是{self.tc}')
class pf3(pf2):
    pass
dx=pf3()  #定义对象
dx.mtd()
dx.pf_m()
dx.pf1_m()

#多层继承
##组合
class pf(object):
    def __init__(self,x):
        self.tc=x
class pf1(object):
    def __init__(self,x):
        self.tc = x
class pf2(object):
    def __init__(self,x,y):
        self.pf = pf(x)
        self.pf1 = pf1(y)
    def pf_m(self):
        print(f'pf2zhong,pf使用技能{self.pf.tc}次,pf1使用技能{self.pf1.tc}次')
dx=pf2(2,3)
dx.pf_m()

class pf(object):
    def __init__(self):
        self.tc='唱歌'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
class pf1(object):
    def __init__(self):
        self.tc = '跳舞'
    def mtd(self):
        print(f'可以继承{self.tc}技能。')
#关联父类
class pf2(pf1,pf):
    def __init__(self):
        self.tc='下棋'
        self.__kh ='lol'   #__ 私有属性
    def get_kh(self):
        return self.__kh
    def set_kh(self):
        self.__kh ='斗地主'
    def __公有方法(self):    #__ 私有方法
        print(f'公用方法')
    def mtd(self):
        print(f'自己的技能是{self.tc}')
    def dy_rest(self,pfc):   #封装成一个函数
        '''调用父类并恢复自身属性'''
        pfc.__init__(self)
        pfc.mtd(self)
        self.__init__()  #将自身属性做初始化恢复自身属性
        print(f'自己的技能是{self.tc}')
    def pf_m(self):
        self.dy_rest(pf) #调用第一个父类
    def pf1_m(self):
        self.dy_rest(pf1) #调用第二个父类
    # def pf_m(self):      #将父类的属性值添加到自身属性里（多个时每个独立添加）
    #     pf.__init__(self)
    #     pf.mtd(self)
    #     self.__init__()    #将自身属性做初始化
    #     print(f'自己的技能是{self.tc}')
    # def pf1_m(self):
    #     pf1.__init__(self)
    #     pf1.mtd(self)
    #     self.__init__()
    #     print(f'自己的技能是{self.tc}')
class pf3(pf2):
    pass
dx=pf3()  #定义对象
dx.mtd()
dx.pf_m()
dx.pf1_m()
#dx.公有方法()  #无法调用
# get_xx  获取私有属性和方法
# set_xx  修改私有属性和方法

dx1=pf2()
dx2=pf3()  #直接通过当前类进行操作所继承的的类的私有属性和方法
#获取私有属性
print(f'修改前获取到：{dx2.get_kh()}')
#修改
dx2.set_kh()
#查看修改后的内容
print(f'修改后获取到：{dx2.get_kh()}')


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
#一次性调用多个父类属性方法  手动调用
    def  ycx(self):
        pf.__init__(self)
        pf.mtd(self)
        pf1.__init__(self)
        pf1.mtd(self)
d4=pf2()
d4.ycx()

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
d5.toget()

class BaseHouse():
    door='原木'
    area=130
    type='三室一厅'
    def opendoor(self):
        print('门可以用钥匙来打开')
    def openwindow(self):
        print('窗户可以用手来推开')
door=BaseHouse()
door.opendoor()


class Company():
    name='酱油科技'
    @classmethod
    def callname(cls):
        print(f'公司名称是：{cls.name}')
Company.callname()


class Fish():
    def __init__(self,name):
        self.name=name
    def skill(self):
        print(f'{self.name}会吐泡泡')
class Goldfish(Fish):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def skill(self):
        print(f'{self.color}的{self.name}会杂技')
g=Goldfish('小金','黄色')
print(g.name,g.color)
g.skill()


class Company():
    def count_num(self):
        print(f'公司目前有xx名员工')
class CompanyA(Company):
    def count_num(self):
        print(f'A公司目前有500名员工')
class CompanyB(Company):
    def count_num(self):
        print(f'B公司目前有300名员工')
class CompanyC(Company):
    def count_num(self):
        print(f'C公司目前有200名员工')

def func(obj):
    obj.count_num()
a=CompanyA() #--new--创建对象 --init-- 添加对象属性
b=CompanyB()
c=CompanyC()
func(a)
func(b)
func(c)

# 子类调用父类的方法
class Public:
    def __init__(self,name,book):
        self.name=name
        self.book=book
    def show(self):
        print(f'出版社：{self.name},书名：{self.book}')
class Pubc(Public):
    def showinfo(self):
        super().show()
io=Pubc('江南出版社','江湖传习录')
io.showinfo()

#多态，多个子类继承同一个父类，每个子类都重写父类的方法
class Public:
    def __init__(self,name,book):
        self.name=name
        self.book=book
    def show(self):
        print(f'出版社：{self.name},书名：{self.book}')
class PublicA(Public):
    def show(self):
        print(f'小明买了一本书，{self.name}的{self.book}')
class PublicB(Public):
    def show(self):
        print(f'小明买了一本{self.name}的{self.book}送给朋友')
n=Public('江南出版社','飞刀又见飞刀')
a=PublicA('华中科技出版协会','论金融风暴的起点和终点')
b=PublicB('西弗出版社','科技与生活')
n.show()
a.show()
b.show()


class Unit:
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    def getstatus(self):
        print(f'玩家：{self.name},生命值：{self.hp},战力为：{self.power}')
class Hero(Unit):
    def __init__(self,hp,power,name):
        super().__init__(hp,power)
        self.name=name
    def getstatus(self):
        print(f'玩家：{self.name},生命值：{self.hp},战力：{self.power}')
class Enemy(Unit):
    def __init__(self,hp,power,name):
        super().__init__(hp,power)
        self.name=name
    def getstatus(self):
        print(f'敌方玩家：{self.name},生命值：{self.hp},战力：{self.power}')
h=Hero(100,50,'LOL')
h.getstatus()
e=Enemy(100,55,'OPO')
e.getstatus()

class Company():
    name='酱油科技'
    @classmethod
    def callname(cls):
        print(f'公司名称是：{cls.name}')
Company.callname()

c=Company()
c.callname()

class Dog():
    __tooth=10
    @classmethod
    def gettooth(cls):
        print(f'weget:{cls.__tooth}')
Dog.gettooth()

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class Company():
    name='Co.,Ltd'
    @classmethod
    def callname(cls,addr):
        print(f'{cls.name}的地址在{addr}')
Company.callname('XINGTANGQU')
d=Company()
d.callname('新塘区')

#修改类属性
#1,内部修改
class Company():
    __name='用友'
    @classmethod
    def modifyname(cls):
        print(f'修改前的类属性为：{cls.__name}')
        cls.__name='长兴科技'
        print(f'修改后的类属性为：{cls.__name}')
Company.modifyname()

class Company():
    name='Co.,Ltd'
    @classmethod
    def callname(cls):
        cls.name='用友'
        cls.addr='北京'
        print(f'{cls.name}在{cls.addr}')
Company.callname()
#外部修改
class Company():
    name='Co.,Ltd'
    @classmethod
    def callname(cls):
        print(f'类属性为：{cls.name}')
Company.callname()
Company.name='用友'
Company.callname()

class Company():
    name='Co.,Ltd'
    @classmethod
    def callname(cls):
        print(f'类属性有：{cls.name}')
Company.callname()
Company.addr='北京'
print(f'类属性有：{Company.name },{Company.addr}')

class Crops():
    cash_crops='棉花'
    food_crops='水稻'
    @classmethod
    def getname(cls):
        print(f'我国的经济农作物是：{cls.cash_crops},粮食农作物是：{cls.food_crops}')
Crops.getname()
c=Crops()
c.getname()


class Class():
    __num=0
    @classmethod
    def addnum(cls):
        cls.__num+=1
    @classmethod
    def getnum(cls):
        print(f'班级人数为：{cls.__num}')
    def __new__(cls):
        Class.addnum()
        return super().__new__(cls)
class Student(Class):
    def __init__(self):
        self.name=''
a=Student()
b=Student()
c=Student()
d=Student()
Class.getnum()

res=random.choices(['男','女'],weights=[0.6,0.4],k=20) #k是选择个数
print(res)


class Human:
    eye=2
    skin='yellow'
    def __new__(cls, name) :
        print('new方法被触发')
        if name=='jack':
            object.__new__(cls) #对象创建的必须


    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
one=Human('name')


class Student():
    school='华科大'
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
    def info(self):
        print(f'{self.school}的学生{self.args[0]}的年龄是{self.args[1]}')
s=Student('leo',22,256,'lol')
s.info()

class Class():
    __num=0
    def __init__(self,name):
        self.name=name

class Yewen():
    def __init__(self,name):
        self.name='叶问'
        self.kongfu='咏春'
    def kong_fu(self):
        print(self.name+'会'+self.kongfu)
class Lixiaolong(Yewen):
    pass
cz=Lixiaolong('czz')
cz.kong_fu()

class Unit:
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    def getstatus(self):
        print(f'玩家：{self.name},生命值：{self.hp},战力为：{self.power}')

class Hero(Unit):
    def __init__(self,hp,power,name):
        super().__init__(hp,power)
        self.name=name

h=Hero(100,120,'jak')
h.getstatus()