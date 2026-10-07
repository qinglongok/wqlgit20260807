import keyword
from operator import index

print(keyword.kwlist)
print('hello\tworld')
print(r'heelo\bworld')
print('hello\bworld')

my_money=30
drink_cost=4
lunch_cost=24
print('午餐后剩余钱数量为：')
print(my_money-drink_cost-lunch_cost)
a=4
b=5

print(a+b)
print(1+1)
print(1/2)
print(3**5)
print(9//4)
print(9%4)
print(9%-4) #一正一负：余数=被除数-除数*商 ;9-(-4)*（—3）

a=1+2+3
print(a)

c,d=10,20
print('交换之前：',c,d)
c,d=d,c
print('交换之后：',c,d)

#m=int(input('请输入一个加数：'))
#n=int(input('请输入另一个加数：'))
#print(m+n)

my_money=30
drink_cost=4
lunch_cost=24
print('午餐后剩余钱数量为：')
print(my_money-drink_cost-lunch_cost)

name='喵喵'
wake_up_hour=10
print("zzz ")
print("＜⌒／ヽ-､_＿_")
print("／＜_/＿＿＿＿／")
print("￣￣￣￣￣￣￣")
print("")
print(f"∧_∧我是{name}")
print(f"(•ω•)我每天{wake_up_hour}点起床")
print("＿|⊃／(＿＿_ ")
print("／└-(＿＿＿_／")
print("￣￣￣￣￣￣￣")


s1='heello world'
print(s1.count("l"))
s2='我们是冠军'
print(s2.count("我们"))
print(len(s1))
print(len(s2))
glj=800
hgr=650
yly=400
kl=330
nc=500
xc=150
tang=300
dw='g'
package1=print(f"{glj}{dw}")
print(package1)

t = (5,6,7)
t1=t[:1]+t[2:]
#t.pop(0)  #元组不能用列表的删除方法
print(t1)
import datetime
a=datetime.datetime.now()
print(a)
#定义类
class dx():
    def __init__(self):
        self.x=x

