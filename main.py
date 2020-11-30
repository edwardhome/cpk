import pandas as pd
import csv

df = pd.read_csv('dataframe.csv')

average = df.mean()
std = df.std()
T = float(input('請輸入規格寬度 = '))
ck = abs((10-average)/(T/2))
cp = T/(6*std)
cpk = (1-ck)*cp

level =[]
for x in cpk.values:
   if x >= 2:
       level.append('perfect')
   elif x<2 and x>=1.33 :
       level.append('Good')
   elif x<1.33 and x>=1 :
       level.append('Notice')
   elif x<1 :
      level.append('Bad')
   else:
       pass

level = pd.Series(level,index=cpk.index)
data = pd.concat([ck,cp,cpk,level],axis=1) #合併表格
data.columns = ['ck','cp','cpk','Level']
print(data)
data.to_csv('data.csv',encoding='utf-8')