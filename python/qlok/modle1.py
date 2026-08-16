def 乘法表():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j}",end="\t")
        print()
if __name__ =='__main__':
    乘法表()

def 乘法表_彩色():
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m',
              '\033[36m', '\033[91m', '\033[92m', '\033[93m']
    reset = '\033[0m'

    for i in range(1, 10):
        for j in range(1, i + 1):
            color = colors[(i + j) % len(colors)]
            print(f"{color}{i}×{j}={i * j:2d}{reset}", end="  ")
        print()

# 在支持颜色的终端运行
if __name__ =='__main__':
    乘法表_彩色()

def database():
    import sqlite3
    import pandas as pd
    import numpy as np
    # 创建连接对象如：conn
    conn = sqlite3.connect(r'D:\pycharm\qlok.db')  # 括号里跟数据库名称#尽量用绝对路径，不然会找不到表
    # 使用连接对象来创建游标对象
    cursor = conn.cursor()
    # 使用游标对象执行sql
    # 获取数据
    path = r'D:\pycharm\test.xlsx'
    df = pd.read_excel(path, sheet_name='users', skiprows=1)
    df = df.map(lambda x: x.replace(" ", "") if isinstance(x, str) else x).replace("", np.nan)
    data = df.values.tolist()  # 每行的值转换成一个列表
    sql = ("select name,password from users ")
    cursor.execute(sql)
    users=cursor.fetchall() #返回元组
    user=[row[0] for row in users]
    password=[row[1] for row in users]
    user_dt=dict(zip(user,password))
    # cursor.executemany(sql,data)  #插入多个值 时要用executemany方法
    # 关闭游标对象
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接对象
    conn.close()
    return user_dt
database()


def add_user(name, password):
        import sqlite3
        conn = sqlite3.connect(r'D:\pycharm\qlok.db')
        cursor = conn.cursor()
        sql = 'insert into users(name,password) values(?,?)'
        cursor.execute(sql, (name, password))
        cursor.close()
        conn.commit()
        conn.close()
        return True

