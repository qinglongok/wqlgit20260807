import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
path=r"C:\Users\qlok\Downloads\2020年广东美迪电器制造有限公司销售收入统计表.xlsx"
df=pd.read_excel(path,header=1)
x=np.arange(len(df.columns[1:]))
print(df.columns[1:])
r=df.columns[1:]
r1=df.iloc[0,1:]
r2=df.iloc[1,1:]
r3=df.iloc[2,1:]
plt.plot(r,r1,label='a',marker='o')
plt.plot(r,r2,label='b',marker='s')
plt.plot(r,r3,label='c',marker='v')
plt.legend()
plt.xlabel('名称/月份')
plt.ylabel('收入/万元')
plt.xticks(x,r1.index)
plt.show()

# plt.clf()  #清空画布
fig,ax=plt.subplots(2,2,figsize=(10,5))  #定义2*2的区域
ax[0,0].plot(r,r1,label='a',marker='o')
ax[0,0].plot(r,r2,label='b',marker='s')
ax[0,0].plot(r,r3,label='c',marker='v')
ax[0,0].legend()
ax[0,0].set_title('折线图')
ax[0,1].barh(r,r1,label='a',facecolor='skyblue')
ax[0,1].barh(r,-r2,label='b',facecolor='red')
ax[0,1].legend()
ax[0,1].set_title('双向条形图')
ax[1,0].hist(r1,label='a',facecolor='lightsalmon')
ax[1,0].legend()
ax[1,0].set_title('直方图',y=-0.3,ha='center')  #直方图：单个指标数据分布情况
ax[1,1].scatter(r2,r3,c='midnightblue',alpha=0.5)
ax[1,1].set_title('散点图',y=-0.3,ha='center')   #散点图：两个指标的相关性分析
plt.show()

fig,ax1=plt.subplots()
width=0.6
ax1.bar(r,r1,width,label='小熊',color='#5BC2E7')
ax1.bar(r,r2,width,bottom=r1,label='智能',color='#51629E')
ax1.bar(r,r3,width,bottom=r1+r2,label='大型',color='#6980C5')
df_t=df.set_index('名称/月份').T #行列转置
cnt=df_t.sum(axis=1)
rate=cnt.pct_change(periods=1)
ax2=plt.twinx()
ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=1))
ax2.plot(r,rate,label=u'增长率')
ax1.legend(loc='upper center')
ax2.legend(loc='upper right')
ax1.set_ylabel('销售收入/万元')
ax2.set_ylabel('销售增长率')
ax1.set_xlabel('月份')
ax1.set_title('2020年广东美迪电器制造有限公司销售收入变动统计表')
plt.tight_layout()
plt.show()

df_t['季节']=['冬季', '冬季', '春季', '春季', '春季', '夏季', '夏季', '夏季', '秋季', '秋季', '秋季', '冬季']
df_t['月合计']=cnt
size=df_t['月合计'].groupby(df_t['季节']).sum()
labels=df_t['季节'].unique().tolist()
explode=(0.05,0,0.2,0)
fig=plt.figure()
ax3=fig.add_subplot()
ax3.pie(size,explode=explode,labels=labels,colors=['red','green','cyan','pink']
        ,autopct='%1.2f%%'
        ,shadow=False
        )
ax3.set_title('2020年广东美迪电器制造有限公司销售收入各季节分布图')
plt.tight_layout()
plt.show()

#玫瑰图
amount=cnt.sort_values()
data=list(amount.index)
plt.figure(figsize=(10,10))
plt.subplot(111,projection='polar')
N=12
theta=np.linspace(0+(100/180)*np.pi,2*np.pi+(100/180)*np.pi,N,endpoint=False)
width=2*np.pi/N
color_list = [
    '#5BC2E7','#6980C5','#51629E',
    '#ff7f0e','#2ca02c','#d62728',
    '#9467bd','#8c564b','#e377c2',
    '#7f7f7f','#bcbd22','#17becf'
]
plt.bar(theta,amount,width=width,bottom=30,color=color_list,edgecolor='black')
# ✅ 强化刻度
plt.tick_params(
    which="major",
    length=9,
    width=1.5,
    color="black",
    labelsize=11
)
# ✅ 强化网格
plt.grid(True, color="#333333", lw=1.1, alpha=0.8)
for a,b,c in zip(theta,amount,data):
    plt.text(a,b+150,str(c),fontsize=15,weight='bold')
plt.title('2020年广东美迪电器制造有限公司销售收入玫瑰图')
plt.tight_layout()
plt.show()
