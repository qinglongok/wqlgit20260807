# #窗体制作
# import tkinter as tk
# from idlelib import window
# from tkinter import messagebox
# from tkinter import filedialog
# def click():
#     text=entry.get()
#     print(f"获取的值为：{text}")
# def change(select):
#     print(f"选择的项目为：{select}")
# def  login():
#     uname=entry1.get()
#     pwd=entry2.get()
#     print(f"登录名：{uname}")
#     print(f"密码：{pwd}")
#
#
# win=tk.Tk()
# win.title('小白窗口设计')
# w=600
# h=400
# sw=win.winfo_screenwidth()
# sh=win.winfo_screenheight()
# x=(sw-w)//2
# y=(sh-h)//2
# win.geometry(f"{w}x{h}+{x}+{y}")
# win.configure(background='white')
# frame1=tk.Frame(win, bg="#FF6B6B",width=200,height=200,relief='raised')
# frame1.grid(row=0,column=0,padx=200,pady=20)
# title=(tk.Label(frame1,text='欢迎使用登陆界面',bg='gold')
#        .grid(row=0,column=0,padx=200,pady=5,sticky='ew'))
# (tk.Frame(frame1, height=3, bg='black')
#        .grid(row=1, column=0, columnspan=3, sticky='ew', pady=(0, 20)))  #分割线条，东西铺满‘ew’
# tk.Label(frame1,text='登录名',bg='pink').grid(row=2,column=0,padx=10,pady=5,sticky='w')
# entry1=(tk.Entry(frame1,width=20,relief='solid')
#         .grid(row=2,column=1,padx=1000,pady=5, sticky='e'))
# entry1=tk.Entry(frame1,width=20,show='*')
# win.mainloop()
#
# lab1=tk.Label(win,text='登录名:',pady=10).grid(row=0,column=0,padx=10,pady=10, sticky='e')
#
# entry1=tk.Entry(win,width=20).grid(row=0,column=1, padx=10,pady=10)
#
# lab2=tk.Label(win,text='密码:',pady=10).grid(row=1,column=0,padx=10, pady=10,sticky='e')
#
# entry2=tk.Entry(win,width=20,show='*')
# entry2.grid(row=1,column=1,padx=10,pady=10)
#
# bt1=tk.Button(win,text='登录',command=login).grid(row=2,column=0,padx=10,pady=10)
# bt2=tk.Button(win,text='取消')
# bt2.grid(row=2,column=1,padx=10)
# option=["唱歌","跳舞","RAP","篮球"]
# selt=tk.StringVar(win)
# selt.set(option[0])
# cj=tk.OptionMenu(win,selt,*option,command=change)
# cj.grid()
# entry=tk.Entry(win)
# entry.grid()
# bt=tk.Button(win,text='测试按钮',command=click)
# bt.grid()
# win.mainloop()

#测试
import tkinter as tk
win = tk.Tk()
win.title("测试窗口")
win.geometry("300x300")
win.resizable(False ,False )
win.config(bg="white")
win.mainloop()

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog
win=tk.Tk()
win.title('小白窗口测试')
w=400
h=300
#定义登录
def login(event=None):
    if var1.get() =='ok' and var2.get() =='123':
       win1=tk.Toplevel(win)
       win1.title('欢迎登陆qlok')
       win1.geometry('300x300+200+100')
       win1.configure(background='pink')
       lab3=tk.Label(win1,text='''
 💞❤💞
 I love you!
 DearLu
 💞❤💞
    试问江湖何处好，
    此心安处是吾乡。
    数声风笛离亭晚，
    君向潇湘我向秦。''',padx=45,pady=10,bg='purple',fg='orange')
       lab3.grid(row=1,column=2,columnspan=3,pady=50,padx=50)
    else:
        msg.showinfo('错误提示','用户名或密码错误！请检查重新输入！')
#重置
def reset(event=None):
    var1.set('')
    var2.set('')

#设置居中
win.geometry(f'{w}x{h}+{(win.winfo_screenwidth()-w)//2}+{(win.winfo_screenheight()-h)//2}')
win.configure(background='white')
#创建用户名标签
lbl1=tk.Label(win,text='用户名:').grid(row=0,column=0,ipadx=10,ipady=10,padx=20,pady=10,sticky='w')
#创建单行输入框
var1=tk.StringVar()
entry1=tk.Entry(win,width=20,textvariable=var1)
entry1.grid(row=0,column=1,columnspan=2)
#创建密码标签
lbl2=tk.Label(win,text='密码:').grid(row=1,column=0,ipadx=10,ipady=10,padx=20,pady=10,sticky='w')
#创建单行输入框
var2=tk.StringVar()
entry2=tk.Entry(win,width=20,show='*',textvariable=var2)
entry2.grid(row=1,column=1,columnspan=2)
#创建登录按钮
bt1=tk.Button(win,text='登录',width=8,command=login)
bt1.grid(row=3,column=1)
#创建重置按钮
bt2=tk.Button(win,text='重置',width=8,command=reset)
bt2.grid(row=3,column=2)
win.bind('<Return>',login)
bt1.bind('<Return>',login)
entry1.focus()
win.mainloop()

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import ttk
wd=tk.Tk()  #定义一个窗口tk(),名为wd
wd.title('古时君曾笑洛阳')
wd.geometry('400x300+200+100')
wd.configure(bg='pink')
def text(event=None):
    va2.set(f'你选的位置是：{va1.get()}')
    if va1.get()=='top':
        msg.showinfo("LOL SelectionPrompt",'you choosed top!')
    elif va1.get()=='jug':
        msg.showinfo("LOL SelectionPrompt",'you choosed jug!')
    elif va1.get()=='mid':
        msg.showinfo("LOL SelectionPrompt",'you choosed mid!')
    elif va1.get() == 'ad':
        msg.showinfo("LOL SelectionPrompt",'you choosed ad!')
    elif va1.get() == 'sup':
        msg.showinfo("LOL SelectionPrompt",'you choosed sup!')
    else:
        msg.showinfo("LOL ErrorPrompt!","Please Choose Right Position!")
bt=tk.Button(wd,text="确认位置",command=text)
bt.grid(row=2,column=1,padx=10,pady=10)
va1=tk.StringVar()
va1.set('top')
combo=ttk.Combobox(wd,textvariable=va1,values=['top','jug','mid','ad','sup'])
combo.bind("<<Combobox>>",text)
combo.grid(row=0,column=1,padx=10,pady=10)
va2=tk.StringVar()
entry1=tk.Entry(wd,textvariable=va2)
entry1.grid(row=1,column=1,padx=10,pady=10)
wd.bind('<Return>',text) #先设置全局回车
bt.bind('<Return>',text) #按钮设置回车
wd.mainloop()

#下拉框combobox方法 在tk下ttk中的combobox方法
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
wd1=tk.Tk()
wd1.title('下拉框测试')
wd1.geometry('400x300+200+100')
wd1.configure(bg='pink')
def tt(event=None):
    if va3.get() not in ['top','jug','mid','ad','sup']:
        msg.showinfo("LOL ErrorPrompt!",f"There Is No {va3.get()}!\nPlease Choose Right Position!")
    else:
        msg.showinfo("LOL SelectionPrompt!",f"you choosed position {va3.get()}!")

va3=tk.StringVar()
combo=ttk.Combobox(wd1,textvariable=va3,values=['top','jug','mid','ad','sup'])
combo.bind("<<ComboboxSelected>>",tt)
combo.grid(row=0,column=1,padx=10,pady=10)
wd1.bind('<Return>',tt)
combo.bind('<Return>',tt)
wd1.mainloop()

