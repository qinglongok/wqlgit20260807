import oracledb
# 数据库配置
user = "SCOTT"        # 你的用户名
pwd = "123456"         # 密码
host = "127.0.0.1"   # 单机本地
port = 1521
service_name = "ORCL" # 你的Oracle服务名

#数据库
#导入模块
import  sqlite3
import pandas as pd
import numpy as np
#创建连接对象如：conn
conn =sqlite3.connect('qlok.db') #括号里跟数据库名称
#使用连接对象来创建游标对象
cursor = conn.cursor()
#使用游标对象执行sql
#获取数据
path=r'D:\pycharm\test.xlsx'
df=pd.read_excel(path,sheet_name='users',skiprows=1)
df=df.map(lambda x: x.replace(" ","") if isinstance(x,str) else x).replace("",np.nan)
data=df.values.tolist() #每行的值转换成一个列表
sql=("select name from users")
cursor.execute(sql)
result=cursor.fetchall()
print(result)
# cursor.executemany(sql,data)  #插入多个值 时要用executemany方法
#关闭游标对象
cursor.close()
#提交事务
conn.commit()
#关闭连接对象
conn.close()




