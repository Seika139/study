import matplotlib.pyplot as plt
import numpy as np
import math


plt.figure(figsize=(3*3,2*3),dpi=128)

PS_x = np.array([0,0.125,0.25,0.5,1])*0.1
PE_x = np.array([0,0.25,0.5,1])*0.1

# 標準液の吸光度
PS_y = np.array([0.079,0.100,0.143,0.183,0.292])
PE_y = np.array([0.079,0.255,0.282,0.727])

# PEの1mlについて
# 0.448 他の班
# 0.727 こぼした

# PSとPE画分の吸光度
PS_t = 0.131
PE_t = 0.252

PS_c = '#223745'
PE_c = '#d08726'

plt.plot(PS_x,PS_y,'.',c=PS_c,label='PS')
plt.plot(PE_x,PE_y,'.',c=PE_c,label='PE')

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
     text = f'y={a:.4f}x\nR={corr:.4f}'
     plt.plot(x, y1, c=color,label=text)
     return a,0

def plot_polyfit(x,y,color):
    # y=ax+b の近似直線を引く
    # 相関係数 Correlation coefficient
    a,b = np.polyfit(x,y,1)
    y2 = a * x + b
    corr = round(np.corrcoef(x,y)[0][1],5)
    text = f'y={a:.4f}x+{b:.4f}\nR={corr:.4f}'
    plt.plot(x,y2,color=color,label=text)
    return a,b

# plot_lr_1(PS_x,PS_y,PS_c)
# plot_lr_1(PE_x,PE_y,PE_c)

a,b = plot_polyfit(PS_x,PS_y,PS_c)
c,d = plot_polyfit(PE_x,PE_y,PE_c)

PS_d = (PS_t - b) / a
PE_d = (PE_t - d) / c

plt.plot(PS_d,PS_t,'*',c='#175da6',label=f'PS_x : {PS_d:.3f}')
plt.plot(PE_d,PE_t,'*',c='#e87e1d',label=f'PE_x : {PE_d:.3f}')

# 画分の濃度 希釈した分を考慮する
PS_n = PS_d*2
PE_n = PE_d*10/3


# PSの量 : 1.5 ml
print(f'PSの濃度 : {PS_n:.4f}mM\nPEの濃度 : {PE_n:.4f}mM')

# チューブに取る量を計算する
PE_2 =  PS_n * 1.5 * 2/3 / PE_n
PE_1 = PE_2 /2

print(f'Tube B : {PE_1:.4f} ml\nTube D : {PE_2:.4f} ml')

plt.title('Calibration curve')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
plt.subplots_adjust(right=0.77)
# plt.subplots_adjust(right=0.8)
plt.xlabel('Consentration(mM)')
plt.ylabel('Absorption')
# グリッド線を引く
plt.grid()
# それぞれの軸の最大値と最小値

plt.savefig('graph.png')
