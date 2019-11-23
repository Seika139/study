# 必要なライブラリのインポート
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats



# データを用意する
ab_test_data = pd.DataFrame({
  "button":["blue", "blue", "red", "red"],
  "result":["press", "not","press", "not"],
  "number":[70, 180, 30, 120]
})
print(ab_test_data)

cross_data = pd.pivot_table(
    data = ab_test_data,
    values ="number",
    aggfunc = "sum",
    index = "button",
    columns = "result"
)
print(cross_data)

stats.chi2_contingency(cross_data, correction=False)


columns = np.array([
    "saline",
    "morphine",
    "naloxone",
    "ibuprofen"
])
c_data = np.array([
1,2,2,1
])
c_data
c_bar = 2-c_data
c_bar
df = pd.DataFrame([c_data,c_bar],columns=columns,index=['t>6','t<=6'])
df
stats.chi2_contingency(df, correction=False)

squared,p,dof,ef = stats.chi2_contingency(df)
print("検定統計量" + str(squared))
print("p値" + str(p))
print("自由度" + str(dof))
print("期待度数"+str(ef))


for i in range(4):
    for j in range(i):
        print(i,j)
