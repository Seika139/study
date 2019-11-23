import matplotlib.pyplot as plt
import numpy as np
import math
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

fig_ratio = np.array([16,9])
fig_times = 0.7
plt.figure(figsize=fig_ratio*fig_times,dpi=128)
x = np.array([0,2.5,5.0,7.5,10,12.5,15,20])

# 標準液の吸光度
y = np.array([
    0.046,
    0.098,
    0.154,
    0.197,
    0.280,
    0.331,
    0.395,
    0.528])
# PSとPE画分の吸光度
sample_y = 0.0075
# サンプルが複数あるときはこっち
sample_ys = np.array([
0.378,
0.404,
0.568,
0.403,
0.631,
0.643,
0.418,
0.390,
])

cl = '#881313'
cl_sp = '#f98600'

plt.plot(x,y,'.',c=cl,label='measured point')

def lr_1(x,y):
    x = np.array(x)
    y = np.array(y)
    a = np.dot(x, y)/(x**2).sum()
    return a

def plot_lr_1(x,y,color):
    # y=ax の近似直線を引く
    # 参考 https://qiita.com/takubb/items/9e3c207b381c3bdd0787
     a = lr_1(x, y)
     y1 = a * x
     corr = round(np.corrcoef(x,y)[0][1],5)
     r2 =  corrr ** 2
     text = f'y={a:.4f}x\nR={corr:.4f}'
     text = f'y={a:.4f}x\nR2={r2:.4f}'
     plt.plot(x, y1, c=color,label=text)
     return a,0

def plot_polyfit(x,y,color):
    # y=ax+b の近似直線を引く
    # 相関係数 Correlation coefficient
    a,b = np.polyfit(x,y,1)
    y2 = a * x + b
    corr = round(np.corrcoef(x,y)[0][1],5)
    r2 = corr**2
    text = f'y={a:.4f}x+{b:.4f}\nR={corr:.4f}'
    text = f'y={a:.4f}x+{b:.4f}\nR2={r2:.4f}'
    plt.plot(x,y2,color=color,label=text)
    return a,b

# plot_lr_1(x,y,cl)
# plot_lr_1(PE_x,PE_y,PE_c)

a,b = plot_polyfit(x,y,cl)

sample_x = (sample_y - b) / a
sample_xs = (sample_ys - b) / a

# plt.plot(sample_x,sample_y,'*',c=cl_sp,label=f'x : {sample_x:.3f}')

# plt.plot(sample_xs,sample_ys,'*',c=cl_sp,label=','.join([str(round(i,3)) for i in sample_xs]))

plt.plot(sample_xs,sample_ys,'*',c=cl_sp)

slides = [(x[-1]-x[0])/30,(y[-1]-y[0])/30]
for i in range(len(sample_xs)):
    plt.text(sample_xs[i]+slides[0],sample_ys[i]-slides[1],np.round(sample_xs[i],3),color=cl_sp)

print(sample_xs)

plt.title('Calibration curve of Opg')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
plt.subplots_adjust(right=0.77)
# plt.subplots_adjust(right=0.8)
plt.xlabel('Consentration(mg/dL)')
plt.ylabel('Absorption')
# グリッド線を引く
plt.grid()
# それぞれの軸の最大値と最小値

plt.savefig(os.path.join(ROOT,'graph-opg.png'))
