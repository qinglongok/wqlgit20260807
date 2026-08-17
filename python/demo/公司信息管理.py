import pandas as pd
import re
path=r"D:\pycharm\test.xlsx"
df=pd.read_excel(path,sheet_name="Sheet4")
df=df.map(lambda x: x.replace(" ","") if isinstance(x,str) else x).replace("",pd.NA)
ls1=df["公司"].iloc[0:].to_list()
ls2=df.iloc[0:,1:6].values.tolist()
# ls3=["ok".join((str(i[0]),str(i[3]))) for i in ls2] #使用join将0和3位置的数据用OK连接
dc=dict(zip(ls1,ls2))
# print(dc)
def search():
    sco=input("请输入你需要用查询的公司名称：")
    if sco in dc:
        print(f"已找到{sco}的信息为：{dc[sco]}")
    else:
        print(f"通讯录里没有{sco}!")
# search()
def add():
    adc=input("请输入需要添加的公司名称：")
    if adc in dc:
        print(f"此公司已经存在，不可重复添加！")
        return
    else:
    #姓名
     while True:
        na=input("请输入所新增公司联系人姓名：").strip()
        if re.match(r'^[\u4e00-\u9fa5a-zA-Z]+$',na) and 0<len(na)<=20:
           print("姓名格式合法！可以使用。")
           break
        else:
            print("姓名格式不合法，请检查重新输入：")
    # na=input("请输入所新增公司联系人姓名：")
    # ag=int(input("请输入联系人年龄："))
    #年龄
     while True:
             ag=int(input("请输入联系人年龄："))
             if isinstance(ag,int) and  18<=ag<=65:
                 print("年龄格式正确")
                 break
             else:
                 print("年龄格式不正确，请检查重新输入：")
    # sx=input("请输入联系人性别：")
    #性别
     while True:
             sx=input("请输入联系人性别：")
             fw=['男','女']
             if sx in fw:
                 print("性别格式正确")
                 break
             else:
                 print("性别格式不正确，请检查重新输入：")
    #联系电话
    #sx=input("请输入联系人性别：")
    while True:
             tl=input("请输入联系人联系电话：")
             if re.match(r'^1\d{10}$',tl):
                print("电话格式正确")
                break
             else:
                 print("手机号格式不正确，请检查重新输入：")
    al = [na, ag, sx, tl]
    dc[adc] = al
    print(f"{adc}信息添加成功！")
    print(f"更新后的信息为：{dc}")
# add()
def delet():
    dn=input("请输入需要删除的公司名称：")
    if dn in dc:
        try:
            del dc[dn]
            print("删除成功")
        except Exception as e:
            print(f"删除失败！{e}")
# delet()

def change():
    oldn=input("请输入需要修改的公司名称：")
    if oldn not in list(dc.keys()):
        print("不存在此公司！")
        return
    else:
            choice=eval(input("请问需要修改什么内容？ 1:公司名称;2:公司联系信息。"))
            if  choice==1:
                    nwn=input("请输入新公司名称：")
                    dc[nwn]=dc.pop(oldn,None) #pop会删除参数键，并返回该键的值
                    print(f"更新完成，{oldn} 名称已更新为：{nwn}")
            elif choice==2:
                print("\033[31m Warning!!!请严格按姓名年龄性别联系电话的顺序输入更新内容！\033[0m")
                cna = input(f"请首先输入所{oldn}修改后的联系人姓名：")
                cag = int(input(f"其次请输入所{oldn}修改后的联系人年龄："))
                csx = input(f"后续请输入所{oldn}修改后的联系人性别：")

                while True:
                    ctl = input(f"最终请输入所{oldn}修改后的联系人联系电话：")
                    if re.match(r'^1\d{10}$', ctl):
                        print("格式正确")
                        break
                    else:
                          print("手机号格式不正确，请检查重新输入：")
                cvl=[cna,cag,csx,ctl]
                dc[oldn]=cvl
                print(f"你成功修改了{oldn}的信息,更新后为：{dc[oldn]}")
                print(f"更新后的信息为：{dc}")

# change()

def main():
    a='欢迎使用客户通讯录'
    b='1.查找 2.添加 3.删除 4.修改 5.返回 6.退出'
    print('{0:=^40}'.format(a))
    print('{0:=^40}'.format(b))
    print("="*51)
    print(dc)   
    while True:
        choice=int(input('请选择你的操作(1.2.3.4.5.6)? \t\n'))
        if choice==1:
              search()
        elif choice==2:
              add()
        elif choice==3:
              delet()
        elif choice==4:
              change()
        elif choice==5:
            while True:
                # 询问是否继续
                confirm = input('\n是否重新运行程序？(y/n): ').lower()
                if  confirm != 'y':
                    print('感谢使用通讯录，期待下次相遇！')
                    break
                else:
                    main()  # 执行主函数
                return
        elif choice==6:
               print('{0:=^42}'.format('感谢使用通讯录，期待下次相遇！'))
        break
if __name__=='__main__':
  main()