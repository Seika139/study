#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリのインポート
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import os

result_path = os.path.join(os.path.dirname(__file__),'result.txt')

raw_data = [
[3,12,2,2],
[3,16,1,3],
[2,15,0,5],
[2,14,4,3]
]

index = ["15min","30min","60min","90min"]
columns = [
    "saline",
    "morphine",
    "naloxone",
    "ibuprofen"
]
master = pd.DataFrame(raw_data,index=index,columns=columns)

with open(result_path,'w') as f:
    f.write("")

for idx,row in master.iterrows():
    text = f'{idx},,\n'
    for i in range(4):
        for j in range(i):
            si = np.array([row[i],row[j]])
            # 今回はマウスの数最大で15*2なので対比の列は2-c
            si_bar = 30 - si
            cl = [columns[i],columns[j]]
            df = pd.DataFrame([si,si_bar],columns=cl)
            squared,p,dof,ef = stats.chi2_contingency(df)
            text += f'{columns[i]}-{columns[j]}'
            yui = '有意差あり' if squared > 3.841 else '有意差なし'
            text += f',{squared:.3f},{yui}\n'
    with open(result_path, 'a') as f:
            f.write(text)
