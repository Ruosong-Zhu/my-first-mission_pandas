import pandas as pd

p = pd.DataFrame(pd.read_excel('C:\\Users\\98243\\Desktop\\配煤\\table\\配合媒质量1-10.1-11.1.xls'))
p = p.dropna(axis=1,how='all')
p1 = p.dropna(subset=['Mt(%)','Mad(%)'],how="all")

time_index = pd.bdate_range(start="2020-10-01",end="2020-10-03",freq="8H")
print(time_index)
