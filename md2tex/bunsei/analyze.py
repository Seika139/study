#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import re
from openpyxl import Workbook


# 必要なディレクトリ(プログラム上)
FILE = 'file1.xlsx'
RESULT = 'result.xlsx'

excel = pd.ExcelFile(FILE)
excel_names = excel.sheet_names
column_list = [
    '1-2',
    '2-3',
    '3-4'
]

for i in range(len(column_list)):
    df = excel.parse(excel_names[0],header=None)
    df = df.dropna()
    df = df[df[i+8]>0.1]
    df[column_list[i]] = (df[i+9]+10**-7)/(df[i+8]+10**-7)
    df.sort_values(column_list[i],ascending=False)
    df = df[:10] # top10を表示
    wb = Workbook()
    wb.new_sheet(column_list[i], data=df.values.tolist())
    wb.save("sample.xlsx")

df = df[df[8]>0.1]
df
df['1-2'] = (df[9]+10**-7)/(df[8]+10**-7)
df
df = df.sort_values('1-2',ascending=False)
df[:1]

df = df.loc[2:,:]
df
df = excel.parse(excel_names[0],header=None)
df = df.dropna()
df = df[df[9]>0.1]
df['2-3'] = (df[10]+10**-7)/(df[9]+10**-7)
df = df.sort_values('2-3',ascending=False)
df

ptn = re.compile('notch')


df1 = excel.parse(excel_names[1],header=None)
df1 = df1.dropna()
df1['notch'] = df1[2].str.contains('notch')
df1 = df1[df1['notch']==True]
df1

df2 = excel.parse(excel_names[0],header=None)
df2 = df2.dropna()
df2['notch'] = df2[2].str.contains('notch')
df2 = df2[df2['notch']==False]
df2 = df2[df2[9]>0.01]
df2['1-2'] = (df2[10]+10**-7)/(df2[9]+10**-7)
df2 = df2.sort_values('1-2',ascending=True)
df2[:10]

df2 = excel.parse(excel_names[0],header=None)
df2 = df2.dropna()
df2 = df2.sort_values(9,ascending=False)
df2

df = excel.parse(excel_names[0],header=None)
df = df.dropna()
rows = [
    18541,
    10630,
    21941
]
for i in rows:
    print(df.loc[i,:])


dfB = excel.parse(excel_names[1],header=None)
dfB = dfB.dropna()
rows = [
    4670,
    9272,
    7737,
    18541,
    11088,
    20256
]
for i in rows:
    print(dfB.loc[i,:])
