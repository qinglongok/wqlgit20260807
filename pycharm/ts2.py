import pandas as pd
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name="Sheet3")
df=df.map(lambda x: x.replace(" ","") if isinstance(x,str) else x)  #使用df.map函数对单元格一个一个处理
df1=df.columns.to_list()
ls1=df['公司'].iloc[0:].dropna().tolist()
print(ls1)
ls2=df.iloc[0:,1:5].values.tolist() #iloc（第一个参数表示第一行索引从0开始，第二个参数表示索引范围（左闭右开））
print(ls2)
dc=dict(zip(ls1,ls2))
print(dc)

import pandas as pd
import re
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name="Sheet3")
df=df.map(lambda x: x.replace(" ","") if isinstance(x,str) else x).replace("",pd.NA)
ls1=df["公司"].iloc[0:].to_list()
print(ls1)
ls2=df.iloc[0:,1:6].values.tolist()
ls3=["ok".join((str(i[0]),str(i[3]))) for i in ls2] #使用join将0和3位置的数据用OK连接
print(ls3)
dc=dict(zip(ls1,ls2))
print(dc)
def search():
    sco=input("请输入你需要用查询的公司名称：")
    if sco in dc:
        print(f"已找到{sco}的信息为：{dc[sco]}")
    else:
        print(f"通讯录里没有{sco}!")
search()
def add():
    adc=input("请输入需要添加的公司名称：")
    if adc in dc:
        print(f"此公司已经存在，不可重复添加！")
    else:
        na=input("请输入所新增公司联系人姓名：")
        ag=int(input("请输入联系人年龄："))
        sx=input("请输入联系人性别：")
        tl=input("请输入联系人联系电话：")
        while True:
            if re.match(r'^1\d{10}$',tl):
                 print("格式正确")
                 break
            else:
                 print("手机号格式不正确，请检查重新输入：")
        al=[na,ag,sx,tl]
        dc[adc]=al
        print(f"{adc}信息添加成功！")
add()
def delet():
    dn=input("请输入需要删除的公司名称：")
    if dn in dc:
        try:
            del dc[dn]
            print("删除成功")
        except Exception as e:
            print(f"删除失败！{e}")
delet()

def change():
    oldn=input("请输入需要修改的公司名称：")
    for name in list(dc.keys()):
        if name == oldn:
            choice=eval(input("请问需要修改什么内容？ 1:公司名称;2:公司联系信息。"))
            if  choice==1:
                    nwn=input("请输入新公司名称！")
                    dc[nwn]=dc.pop(name,None) #pop会删除参数键，并返回该键的值
                    print(f"更新完成，更新后数据为：{dc}")
            elif choice==2:
                     cna = input("请输入所新增公司联系人姓名：")
                     cag = int(input("请输入联系人年龄："))
                     csx = input("请输入联系人性别：")
                     ctl = input("请输入联系人联系电话：")
            while True:
                     if re.match(r'^1\d{10}$', ctl):
                        print("格式正确")
                        break
                     else:
                          print("手机号格式不正确，请检查重新输入：")
        cvl=[cna,cag,csx,ctl]
        dc[oldn]=cvl
        print(f"你成功修改了{oldn}的信息,更新后为：{dc[oldn]}")
        break
    else:
           print("不存在此公司！")
change()

def main():
    a='客户通讯录'
    b='1.查找 2.添加 3.删除 4.修改 5.退出'
    print('{0:=^40}'.format(a))
    print('{0:=40}'.format(b))
    print("="*51)
    while True:
        chioce=eval(input('请选择你的操作(1.2.3.4.5)?\n'))
        if chioce==1:
              search()
        elif chioce==2:
              add()
        elif chioce==3:
              delet()
        elif chioce==4:
              change()
        elif chioce==5:
               print('{0:=^42}'.format('感谢使用通讯录，期待下次相遇！'))
        break
if __name__=='__main__':
  main()
