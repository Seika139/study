import matplotlib.pyplot as plt
import numpy as np
import os

"""
用量作用曲線を書くためのプログラム
"""

ROOT = os.path.abspath(os.path.dirname(__file__))

def plotter(x,y,c,label,linestyle):
    plt.plot(x,y,'-',c=c,label=label,linestyle=linestyle)


def main():
    fig_ratio = np.array([16,9])
    fig_times = 0.7
    plt.figure(figsize=fig_ratio*fig_times,dpi=128)

    x10 = np.array(range(-18,-8,1)) /2
    x12 = np.array(range(-18,-6,1)) /2

    y2 = np.array([
    0,0,0,0,62.5,84.375,92.1875,96.875,99.0625,100
    ])
    y3 = np.array([
    0,0,0,0,0,0,0,16.25,62.5,85.3125,100,100
    ])
    y4 = np.array([
    0,0,0,0,0,0,0,0,0,25,84.375,100
    ])
    y5 = np.array([
    0,0,0,0,0,7.5,60.3125,76.875,81.875,76.875,75.625,74.375
    ])

    labels = ['Control','Atropine -8','Atropine -7','Papaverine']
    colors = ['#aa0957','#1ed6c0','#2945d9','#1ceb24']
    linestyles = ['solid', 'dotted','dashed', 'dashdot']

    for i,y in enumerate([y2,y3,y4,y5]):
        if i==0:
            if len(y) != 10:
                print(i,'invalid length')
            plotter(x10,y,colors[i],labels[i],linestyles[i])
        else:
            if len(y) != 12:
                print(i,'invalid length')
            plotter(x12,y,colors[i],labels[i],linestyles[i])

    plt.title('Dose response curve')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
    plt.subplots_adjust(right=0.77)
    # plt.subplots_adjust(right=0.8)
    plt.xlabel('Concentration (log_10^C)')
    plt.ylabel('Shrinkage ratio (%)')
    # グリッド線を引く
    plt.grid()
    # それぞれの軸の最大値と最小値

    plt.savefig(os.path.join(ROOT,'ys_curve.png'))


if __name__ == "__main__":
    main()
