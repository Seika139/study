#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd

# 必要なディレクトリ(プログラム上)
# __file__ = 'bunsei/not_notch.py'
ROOT = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(ROOT,'file1.xlsx')
RESULT = os.path.join(ROOT,'result-2.xlsx')

excel = pd.ExcelFile(FILE)
excel_names = excel.sheet_names
df = excel.parse(excel_names[1],header=None)
df = df.dropna()

# notch を含まないもののみ選択
df['notch'] = df[2].str.contains('notch')
df = df[df['notch']==False]

df = df[df[8]>0.1]
df['E12-E13'] = (df[9]+10**-7)/(df[8]+10**-7)
df = df.sort_values('E12-E13',ascending=False)
df = df[:10] # top10を表示
df.to_excel(RESULT)
