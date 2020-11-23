import pandas as pd
import numpy as np

# 生成‘白’‘中’‘夜’时间序列
# time_index = pd.Series(pd.bdate_range(start='2019-01-01',end='2020-10-01',freq="8H"))
# time_index = time_index[:-1]

p = pd.DataFrame(pd.read_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\1\\row\\PHM-20190101-20200930.xls'))

## 1.列中全为NAT，则删除 2.按是否进行基本工业分析，删除取样失败的行
p = p.dropna(axis=1,how='all')
p = p.dropna(subset=['Mad(%)','Ad(%)','Vdaf(%)','Fcad(%)'],how="all")
p = p[:-1]
p = p.reset_index(drop=True)
p = p.sort_index(ascending=False,ignore_index=True)

time_index_p = p['取样时刻'].values.astype('datetime64[D]')
time_index_p = pd.Series(time_index_p).T
## 测试用：DataFrame取差
# delete_what_p = p1.append(p).drop_duplicates(keep=False)

result_BlendedCoal = pd.concat([time_index_p,p],axis=1)
result_BlendedCoal.rename(columns = {0:'Time'},inplace = True)
useless1 = ['选择','检验委托号','取样日期','取样位置','取样编号','制样编码','取样类别(C)','取样方式','样序号','品名代码','班别','备注']
result_BlendedCoal.drop(labels=useless1,axis=1,inplace=True)


lj = pd.DataFrame(pd.read_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\1\\row\\YJJ-20190101-20200930.xls'))
lj = lj[:-1]

#去除‘水分分析’‘DC(抽样)’
lj = lj[~lj['分析类别'].isin(["水分分析"])]
lj = lj[~lj['取样类别'].isin(["DC"])]
lj = lj.dropna(subset=['M40(%)','M10(%)','Ad(%)','Vdaf(%)'],how="any")

#删除多余列
useless2 = ['样序号','考核','选择','制样编码','检验委托号','取样方式','品名','班别','产量','冶金焦干熄焦','等级','取样类别(C)']
lj.drop(labels=useless2,axis=1,inplace=True)

#取出CK
dict_CK= {}
x = 0
for i in range (len(lj)):
    for j in range(lj.shape[1]):
         if lj.iloc[i,j] == "CK":
            dict_CK[x]=lj.iloc[i,:]
            x = x+1
dict_CK = pd.DataFrame(dict_CK).T
# print(dict_CK)

lj = lj[~lj['取样类别'].isin(["CK"])]


# for i,j,k in zip (lj['取样类别'],lj['CRI(%)'],lj['CSR(%)']):
#   # if i == "CK":
#     print(i)
# print(lj.shape[1])

#重排列
lj = lj.sort_index(ascending=False,ignore_index=True)
lj = lj.reset_index(drop=True)

result_Coke = lj
# result_LJ = pd.concat([time_index,lj],axis=1)
result_Coke.rename(columns = {'取样日期':'Time'},inplace = True)

# ang = time_index_p.iloc[1]-time_index_lj.iloc[0]

result = pd.merge(left=result_BlendedCoal,right=result_Coke,on=['Time','班次'])

# result_BlendedCoal.to_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\1\\R-PHM-20190101-20200930.xlsx')
# result_LJ.to_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\1\\R-LJ-20190101-20200930.xlsx')
result.to_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\1\\test-result-20190101-20200930.xlsx')