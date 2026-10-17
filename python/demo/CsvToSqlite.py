import requests
import datetime
from translate import Translator
import csv
import sqlite3
import hashlib
import random
import time
from 装饰器 import count_t
class CsvToSqlite():
    '''其它文件需要重新修改path_csv和table_name两个参数'''
    path_csv=r"D:\pycharm\双色球.csv"
    table_name="double_color_ball"
    APP_ID = "20261018002702507"
    APP_KEY = "r5j7dyNwz9e65nyCffjT"
    def __init__(self):
        self.conn = sqlite3.connect(r"D:\pycharm\qlok.db")
        self.cur = self.conn.cursor()

    @count_t
    def get_new_csvdata(self):
        try:
            f=open('双色球.csv',mode='w',newline='',encoding='utf-8-sig')
            csv_writer=csv.DictWriter(f,fieldnames=[
                  '期数',
                  '开奖日期',
                  '全国中奖详情',
                  '红球',
                  '蓝球',
                  '奖池',
                  '一等奖中奖注数',
                  '一等奖中奖金额',
                  '二等奖中奖注数',
                  '二等奖中奖金额',
                  '三等奖中奖注数',
                  '三等奖中奖金额',
                  '四等奖中奖注数',
                  '四等奖中奖金额',
                  '五等奖中奖注数',
                  '五等奖中奖金额',
            ],)
            csv_writer.writeheader()
        except Exception as e:
            self.show_time(e)
        for page in range(1,72):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Cookie':'21_vq=6'
                ,'Referer':'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'
            }
            url='https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'
            date=datetime.datetime.now().strftime("%Y-%m-%d")
            params={
                    'name':'ssq',
                    'issueCount':'',
                    'issueStart':'',
                    'issueEnd':'',
                    'dayStart':'2013-01-01',
                    'dayEnd':date,
                    'pageNo':page,
                    'pageSize':'30',
                    'week':'',
                    'systemType':'PC',
            }
            resp = requests.get(url, headers=headers,params=params)
            try:
                text=resp.text.replace(r"\'", "'")
                result=resp.json()['result']
                for item in result:
                    dic={
                        '期数':item['code'],
                        '开奖日期': item['date'],
                        '全国中奖详情':item['content'],
                        '红球':item['red'],
                        '蓝球':item['blue'],
                        '奖池':item['poolmoney'],
                        '一等奖中奖注数':item['prizegrades'][0]['typenum'],
                        '一等奖中奖金额':item['prizegrades'][0]['typemoney'],
                        '二等奖中奖注数':item['prizegrades'][1]['typenum'],
                        '二等奖中奖金额':item['prizegrades'][1]['typemoney'],
                        '三等奖中奖注数':item['prizegrades'][2]['typenum'],
                        '三等奖中奖金额':item['prizegrades'][2]['typemoney'],
                        '四等奖中奖注数': item['prizegrades'][3]['typenum'],
                        '四等奖中奖金额': item['prizegrades'][3]['typemoney'],
                        '五等奖中奖注数': item['prizegrades'][4]['typenum'],
                        '五等奖中奖金额': item['prizegrades'][4]['typemoney'],

                    }
                    csv_writer.writerow(dic)
            except Exception as e:
                self.show_time(e)
            self.show_time(f'第{page}页爬取完成')
    def show_time(self,*args,**kwargs):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'[{now}]\033[36m info:\033[0m',*args,**kwargs)
    def get_csv(self):
        with open(self.path_csv, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            zh_col=reader.fieldnames
            rows=list(reader)
            return zh_col,rows
    def get_col_name(self):
        '''提取列名(英文字段名)'''
        sql1 = f'PRAGMA table_info({self.table_name})'  # 查询列名
        self.cur.execute(sql1)
        res = self.cur.fetchall()
        col_name = [item[1] for item in res]  # 列表推导式，直接将结果报错为列表
        return col_name
    def to_zh(self,word):
        '''需使用网络访问网页进行翻译速度较慢，备用方法'''
        translator=Translator(from_lang="zh",to_lang="en")
        res=translator.translate(f"{word}").replace(' ','_')
        return res
    def baidu_translate(self,q, from_lang="zh", to_lang="en") :
        url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
        salt = random.randint(1, 999999)
        sign = hashlib.md5(f"{self.APP_ID}{q}{salt}{self.APP_KEY}".encode()).hexdigest()
        params = {
            "q": q,
            "from": from_lang,
            "to": to_lang,
            "appid": self.APP_ID,
            "salt": salt,
            "sign": sign
        }
        resp = requests.get(url, params=params)
        res = resp.json()
        time.sleep(1.2)
        if "trans_result" in res:
            return res["trans_result"][0]["dst"].replace(' ','_')
        else:
            c=CsvToSqlite()
            return c.show_time("API错误：", res)
    def create_table(self):
        '''读取csv 并根据csv列名转化成英文后作为字段名建表'''
        # with open(self.path_csv, encoding="utf-8-sig", newline="") as f:  # utf-8-sig读取时自动去掉开头的BOM(文本开头的标签字节)字节
        #     reader = csv.DictReader(f)  # DictReader自动读取第一行，存到fieldnames作为表头
        #     headers = reader.fieldnames
        res=self.get_csv()
        headers=res[0]
        col_def = []
        for col in headers:
            if col == '期数':
                d=CsvToSqlite()
                col_def.append(f'{d.baidu_translate(col)} TEXT PRIMARY KEY')
            else:
                col_def.append(f'{d.baidu_translate(col)} TEXT')
        ct = ",".join(col_def)
        sql=f'create table if not exists {self.table_name} ({",".join(col_def)})'
        self.cur.execute(sql)
        self.conn.commit()
    def insert_data(self):
        colname=self.get_col_name()
        cols=",".join(colname)
        p_values=",".join("?"*len(colname))
        insert_sql=f'insert or ignore into {self.table_name}({cols}) values({p_values})'
        cnt=0
        res1 = self.get_csv()
        '''获取到csv源文件的表头列表在中文'''
        csv_colname=res1[0]
        reader=res1[1]
        '''循环插入csv行'''
        for row in reader:
            values=[row[col] for col in csv_colname]
            self.cur.execute(insert_sql, values)
            cnt+=1
        self.conn.commit()
        self.show_time(f'{f"导入完成，共导入{cnt}条数据":-^40}')
    def clear_table(self):
        '''清空数据'''
        sql=f'delete from {self.table_name}'
        self.cur.execute(sql)
        self.conn.commit()
        self.show_time(f'{self.table_name} 数据已清空，删除行数：{self.cur.rowcount}')
        self.show_time(f'{self.table_name} 开始导入数据')
    @count_t
    def check_table_exists(self):
        sql="SELECT name FROM sqlite_master WHERE type='table';"
        self.cur.execute(sql)
        res=self.cur.fetchall()
        table_list = []
        for h in res:
            table_list.append(*list(h))
        if self.table_name in table_list:
            self.show_time(f'{"表已经存在,开始清空表数据":-^40}')
            self.clear_table()
            self.insert_data()
        else:
            self.show_time(f'{f"{self.table_name}不存在,开始创建表格":-^40}')
            self.create_table()
            self.show_time('表格创建完成')

if __name__=='__main__':
    obj=CsvToSqlite()
    obj.get_new_csvdata()
    obj.check_table_exists()

'''drafts'''
#     def er():
#         sql="SELECT name FROM sqlite_master WHERE type='table';" #查询表名
#         self.cur.execute(sql)
#         res=self.cur.fetchall()
#         table_list=[]
#         for h in res:
#             table_list.append(*list(h))
#         if table_name in table_list:
#             print('表已建好')
#             '''提取列名'''
#             sql1=f'PRAGMA table_info({table_name})' #查询列名
#             self.cur.execute(sql1)
#             res=self.cur.fetchall()
#             col_name=[item[1] for item in res] #列表推导式，直接将结果报错为列表
#         else:
#             print('表不存在')
#             create_table()
#     # show_time(baidu_translate('红球'))
#     # exit()
# with open(path_csv, encoding="utf-8-sig", newline="") as f: #utf-8-sig读取时自动去掉开头的BOM(文本开头的标签字节)字节
#     reader = csv.DictReader(f) #DictReader自动读取第一行，存到fieldnames作为表头
#     headers = reader.fieldnames
#     show_time(headers)
#     col_def=[]
#     for col in headers:
#         if col=='期数':
#             col_def.append(f'{baidu_translate(col)} TEXT PRIMARY KEY')
#             show_time(col_def)
#         else:
#             col_def.append(f'{baidu_translate(col)} TEXT')
#     ct=",".join(col_def)
#     # show_time(ct)
#     # sql=f'create table if not exists {table_name} ({",".join(col_def)})'
#     # self.cur.execute(sql)
#     # conn.commit()
#     '''sqlite 插入语句：insert or ignore into tablename(col1,col2,...) values(?,?...)
#        values必须与前面的列保持一致
#     '''
#     #插入数据，遇到重复期数直接跳过
#     list_header=[c for c in col_def]
#     cols=",".join(list_header)
#     list2_values=",".join("?"*len(headers))
#     show_time(list2_values)
#     print(len(headers))
#     insert_sql=f'insert or ignore into {table_name} ({cols}) values ({list2_values})'
#     print(insert_sql)
#     exit()
#     '''记录查询条数'''
#     cnt=0
#     for row in reader:
#         values=[row[col] for col in headers]
#         show_time(values)
#         self.cur.execute(insert_sql, values)
#         cnt+=1
#         conn.commit()
#         exit()
#
#     # insert_cols = ",".join([f'"{c}"' for c in fieldnames])
#     # placeholders = ",".join(["?"] * len(fieldnames))
#     # insert_1= f'INSERT OR IGNORE INTO {TABLE_NAME} ({insert_cols}) VALUES ({placeholders})'
#     exit()
#     reader = csv.DictReader(f)
# #             fieldnames = reader.fieldnames
# #             logging.info(f"读取CSV字段: {fieldnames}")
# #
# #             # 构建建表语句，全部字段默认文本类型，简单通用
# #             col_defs = []
# #             for col in fieldnames:
# #                 if col == PRIMARY_KEY:
# #                     col_defs.append(f'"{col}" TEXT PRIMARY KEY')
# #                 else:
# #                     col_defs.append(f'"{col}" TEXT')
# #             create_sql = f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({",".join(col_defs)})'
# #             self.cur.execute(create_sql)
# #             conn.commit()
# # try:
# #     f=open('双色球.csv',mode='w',newline='',encoding='utf-8-sig')
# #     csv_writer=csv.DictWriter(f,fieldnames=[
# #           '期数',
# #           '开奖日期',
# #           '全国中奖详情',
# #           '红球',
# #           '蓝球',
# #           '奖池',
# #           '一等奖中奖注数',
# #           '一等奖中奖金额',
# #           '二等奖中奖注数',
# #           '二等奖中奖金额',
# #           '三等奖中奖注数',
# #           '三等奖中奖金额',
# #           '四等奖中奖注数',
# #           '四等奖中奖金额',
# #           '五等奖中奖注数',
# #           '五等奖中奖金额',
# #     ],)
# #     csv_writer.writeheader()
# # except Exception as e:
# #     print(e)
# # for page in range(1,72):
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
# #         'Cookie':'21_vq=6'
# #         ,'Referer':'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'
# #     }
# #     url='https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'
# #     num=1
# #     date=datetime.datetime.now().strftime("%Y-%m-%d")
# #     params={
# #             'name':'ssq',
# #             'issueCount':'',
# #             'issueStart':'',
# #             'issueEnd':'',
# #             'dayStart':'2013-01-01',
# #             'dayEnd':date,
# #             'pageNo':page,
# #             'pageSize':'30',
# #             'week':'',
# #             'systemType':'PC',
# #     }
# #     resp = requests.get(url, headers=headers,params=params)
# #     try:
# #         text=resp.text.replace(r"\'", "'")
# #         result=resp.json()['result']
# #         for item in result:
# #             dic={
# #                 '期数':item['code'],
# #                 '开奖日期': item['date'],
# #                 '全国中奖详情':item['content'],
# #                 '红球':item['red'],
# #                 '蓝球':item['blue'],
# #                 '奖池':item['poolmoney'],
# #                 '一等奖中奖注数':item['prizegrades'][0]['typenum'],
# #                 '一等奖中奖金额':item['prizegrades'][0]['typemoney'],
# #                 '二等奖中奖注数':item['prizegrades'][1]['typenum'],
# #                 '二等奖中奖金额':item['prizegrades'][1]['typemoney'],
# #                 '三等奖中奖注数':item['prizegrades'][2]['typenum'],
# #                 '三等奖中奖金额':item['prizegrades'][2]['typemoney'],
# #                 '四等奖中奖注数': item['prizegrades'][3]['typenum'],
# #                 '四等奖中奖金额': item['prizegrades'][3]['typemoney'],
# #                 '五等奖中奖注数': item['prizegrades'][4]['typenum'],
# #                 '五等奖中奖金额': item['prizegrades'][4]['typemoney'],
# #
# #             }
# #             csv_writer.writerow(dic)
# #     except Exception as e:
# #         print(e)
# #     print(f'第{page}页爬取完成')
# #
# # import csv
# # import sqlite3
# # import logging
# #
# # # ========== 配置区，自行修改路径 ==========
# # CSV_PATH = r"D:\pycharm\lottery.csv"
# # DB_PATH = r"D:\pycharm\lottery.db"
# # TABLE_NAME = "lottery_data"
# # # 期数作为唯一主键，防止重复导入同一期数据
# # PRIMARY_KEY = "期数"
# #
# # # 日志配置
# # logging.basicConfig(
# #     filename="D:/pycharm/spider.log",
# #     encoding="utf-8",
# #     format="%(asctime)s %(levelname)s: %(message)s",
# #     level=logging.INFO
# # )
# #
# # def csv_to_sqlite():
# #     conn = None
# #     try:
# #         conn = sqlite3.connect(DB_PATH)
# #         self.cur = conn.cursor()
# #
# #         # 读取CSV表头
# #         with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
# #             reader = csv.DictReader(f)
# #             fieldnames = reader.fieldnames
# #             logging.info(f"读取CSV字段: {fieldnames}")
# #
# #             # 构建建表语句，全部字段默认文本类型，简单通用
# #             col_defs = []
# #             for col in fieldnames:
# #                 if col == PRIMARY_KEY:
# #                     col_defs.append(f'"{col}" TEXT PRIMARY KEY')
# #                 else:
# #                     col_defs.append(f'"{col}" TEXT')
# #             create_sql = f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({",".join(col_defs)})'
# #             self.cur.execute(create_sql)
# #             conn.commit()
# #
# #             # 插入数据，遇到重复期数直接跳过
# #             insert_cols = ",".join([f'"{c}"' for c in fieldnames])
# #             placeholders = ",".join(["?"] * len(fieldnames))
# #             insert_sql = f'INSERT OR IGNORE INTO {TABLE_NAME} ({insert_cols}) VALUES ({placeholders})'
# #
# #             count = 0
# #             for row in reader:
# #                 values = [row[c] for c in fieldnames]
# #                 self.cur.execute(insert_sql, values)
# #                 count += 1
# #             conn.commit()
# #             logging.info(f"导入完成，共处理 {count} 条记录")
# #
# #     except Exception as e:
# #         logging.error("CSV导入SQLite失败", exc_info=True)
# #     finally:
# #         if conn:
# #             conn.close()
# #
# # if __name__ == "__main__":
# #     csv_to_sqlite()
