import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog

win1=tk.Tk()
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
win1.mainloop()





















