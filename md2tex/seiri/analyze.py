# usr/bin/env python
# coding: utf-8

import math
import numpy as np
import os
import pandas as pd

df = pd.read_csv('Results.csv')
array = df['Mean'].tolist()

all = np.average(df['Mean'][:2])
blank = np.average(df['Mean'][2:4])

all,blank

df1 = df[6:22]
df1['Mean']-blank
df1['b/t(%)'] = (df1['Mean']-blank)/(all-blank)*100

list_conc = []
for i in range(len(df1)//2):
    for _ in range(2):
        list_conc.append(0.625*2**i)
df1['conc'] = list_conc
print(df1)
