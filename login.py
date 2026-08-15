import tkinter as tk
import webbrowser
import re
from setuptools import command
import modle1
from tkinter import messagebox as msg
from PIL import ImageTk,Image
win=tk.Tk()
win.title('Welcome To My Home page!')
win.geometry('400x300+200+100')
win.configure(bg='pink')
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
canvas=tk.Canvas(win,highlightthickness=0)
canvas.grid(row=0,column=0,sticky='nsew')
image=Image.open(r"C:\Users\qlok\Desktop\R-C.jpg")
image = image.resize((400, 300), Image.Resampling.LANCZOS) ##图片高质量缩放参数
pt=ImageTk.PhotoImage(image)
canvas.create_image(0,0,image=pt,anchor='nw')
canvas.image=pt

#创建登录函数
def login(event=None):
    user = modle1.database()
    name=va1.get().strip()
    password = va2.get().strip()
    if not name:
        msg.showwarning('错误提示！','输入用户名为空，请输入用户名！')
        entry1.focus() #光标回到用户名栏
        return
    if not password:
        msg.showwarning('错误提示！', '输入密码为空，请输入用户名！')
        entry2.focus() #光标回到密码栏
        return
    if any(name in k for k in user.keys())==True:
        if  password == user.setdefault('qlok', None):
            msg.showinfo('欢迎登录!', '登录成功，按回车立即跳转界面>>>')
            webbrowser.open_new_tab('https://www.baidu.com')
        else:
            msg.showerror('Error!', 'tp:密码错误！请检查重新输入！')
    else:
            msg.showerror('Error!', 'tp:用户名不存在')

#重置函数
def reset(event=None):
    va1.set('')
    va2.set('')

def register_ck(event=None):
    win1 = tk.Toplevel(win)
    win1.title('欢迎进入注册界面')
    win1.geometry('400x300+600+100')
    win1.configure(bg='pink')
    win1.grid_rowconfigure(0, weight=1)
    win1.grid_columnconfigure(0, weight=1)
    canvas1 = tk.Canvas(win1, highlightthickness=0)
    canvas1.grid(row=0, column=0, sticky='nsew')
    try:
        canvas1.create_image(0, 0, image=pt,anchor='nw')
        image1 = Image.open(r"C:\Users\qlok\Desktop\R-C.jpg")
        image1 = image.resize((400, 300), Image.Resampling.LANCZOS)
        pt1 = ImageTk.PhotoImage(image1)
        canvas1.create_image(0, 0, image=pt1, anchor='nw')
        canvas1.image = pt1
    except:
        canvas1.configure(bg='pink')
    va3 = tk.StringVar()
    entry3 = tk.Entry(win1, font=("Arial", 15), width=15, textvariable=va3)
    canvas1.create_window(200, 100, window=entry3)
    lb3 = tk.Label(win1, text='用户名')
    canvas1.create_window(50, 100, window=lb3)
    va4 = tk.StringVar()
    entry4 = tk.Entry(win1, font=("Arial", 15), width=15, textvariable=va4)
    canvas1.create_window(200, 200, window=entry4)
    lb4 = tk.Label(win1, text='密  码')
    canvas1.create_window(50, 200, window=lb4)
    def register_confirm():
        name=va3.get().strip()
        password=va4.get().strip()
        user_dict = modle1.database()
        if not name:
            msg.showerror('错误信息', '注册失败,用户名不能为空！')
            entry3.focus()
            return
        if name in user_dict.keys():
            msg.showerror('错误信息', '注册失败,用户名已被占用！')
            entry3.focus()
            return
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$',name):
            msg.showerror('错误信息', '注册失败,用户名格式不合规！')
            entry3.focus()
            return
        if not password:
            msg.showerror('错误信息', '注册失败,密码不能为空！')
            entry4.focus()
            return
        if not re.match(r'^[0-9]+$',password) :
            msg.showerror('错误信息', '注册失败,密码必须为纯数字！')
            entry4.focus()
            return
        if len(password)<6 or len(password)>20:
            msg.showerror('错误信息', '注册失败,密码长度为6-20！')
            entry4.focus()
            return
        try:
            success=modle1.add_user(va3.get(), va4.get())
            if success:
                msg.showinfo('提示信息','注册成功')
                win1.destroy()
            else:
                 msg.showerror('错误信息','注册失败')
        except Exception as e:
            msg.showerror('错误信息',f'注册失败:{str(e)}')
    bt4 = tk.Button(win1, text='确认注册', command=register_confirm)
    canvas1.create_window(200, 250, window=bt4)
    win1.bind('<Return>',lambda e:register_confirm())
    bt4.bind('<Return>', lambda e:register_confirm())

def get_more():
    webbrowser.open_new_tab('https://www.baidu.com')

def on_closing():
    if msg.askokcancel("退出", "你确定要退出吗？"):
        win.destroy()
#布局
label = tk.Label(win, text="Welcome TO Epiphany",\
                 font=("微软雅黑",20,"bold"),bg='#FFE4B5',relief='flat',highlightthickness=0)
canvas.create_window(200, 50, window=label)

label1=tk.Label( win, text="用户名",\
                 font=("仿宋",15,"bold"),bg='#00FFFF',relief='flat',highlightthickness=0)
canvas.create_window(52, 100, window=label1)
label2=tk.Label( win, text="密  码",\
                 font=("仿宋",15,"bold"),bg='#00FFFF',relief='flat',highlightthickness=0)
canvas.create_window(52, 150, window=label2)
bt1=tk.Button(win, text="登录",font=("仿宋",18,"bold"),bg='#DA70D6',\
              relief='flat',highlightthickness=0,command=login)
canvas.create_window(155, 200, window=bt1)

bt2=tk.Button(win, text="重置", font=("仿宋",18,"bold"),bg='#A9A9A9',\
              relief='flat',highlightthickness=0,command=reset)
canvas.create_window(290, 200, window=bt2)

bt3=tk.Button(win, text="注册",\
                 font=("仿宋",12,"bold"),bg='#8BC34A',\
                 relief='flat',highlightthickness=0,command=register_ck)
canvas.create_window(50, 260, window=bt3)
bt3=tk.Button(win, text="获取更多>>>",\
                 font=("仿宋",12,"bold"),bg='#CD853F',relief='flat',\
                 highlightthickness=0,command=get_more)
canvas.create_window(310, 260, window=bt3)

va1=tk.StringVar()
entry1=tk.Entry(win,font=("Arial", 18), width=17,textvariable=va1)
canvas.create_window(220,100, window=entry1)
va2=tk.StringVar()
entry2=tk.Entry(win,font=("Arial", 18), width=17,textvariable=va2)
canvas.create_window(220,150, window=entry2)
# lb1=tk.Label(win,text='用户名',bg='purple')
# lb1.grid(row=0,column=0,ipadx=10,ipady=10,padx=20,pady=10,sticky='w')
# va1=tk.StringVar()
# entrr1=tk.Entry(win,textvariable=va1)
# entrr1.grid(row=0,column=1)
# lb2=tk.Label(win,text='密码',bg='purple')
# lb2.grid(row=1,column=0,ipadx=10,ipady=10,padx=20,pady=10,sticky='w')
# va2=tk.StringVar()
# enrr2=tk.Entry(win,textvariable=va2)
# enrr2.grid(row=1,column=1)
# user=modle1.database()
# print(user.setdefault('qlok',None))
# if  any('qlok'  in k for k in user.keys()) == True:
#     msg.showinfo('Prompt!', '输入用户名正确！')
#     if password == user.setdefault('qlok', None):
#         msg.showinfo('Prompt!', '输入密码正确！')
#     else:
#         msg.showerror('Error!', 'tp:密码错误！请检查重新输入！')
# else:
#     msg.showerror('Error!', 'tp:用户名不存在')

# if 'qlok' not in user:
#         msg.showerror('Error!','tp:用户名不存在')
# elif password == user.setdefault('qlok',None):
#         print('Welcome To My Home page!')
#     else:
#         print('用户名不存在！')



win.bind('<Return>',login)
bt1.bind('<Return>',login)
win.mainloop()