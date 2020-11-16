
import requests
par={'servicename':'pmomhr03_inq',\
'p_string':'NEXT_WHOLE_BACKLOG_CODE,H2',\
'ret_table':'','userid':'','username':''}
url={0:'http://172.16.2.158:8101/as_lzirm1.asmx/CallServerJson',\
1:'http://172.16.2.158:8102/as_lzlsm1.asmx/CallServerJson',\
2:'http://172.16.2.158:8103/as_lzmms1.asmx/CallServerJson',\
3:'http://172.16.2.158:8105/as_lzpea1.asmx/CallServerJson',\
4:'http://172.16.2.158:8106/as_lzpeb1.asmx/CallServerJson',\
5:'http://172.16.2.158:8107/as_lzpec1.asmx/CallServerJson',\
6:'http://172.16.2.158:8108/as_lzped1.asmx/CallServerJson'}

## http://172.16.2.158:8105/as_lzpea1.asmx/CallServerJson Iron area
r=requests.post(url[2],par)

from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parseString(r.text)
collection = DOMTree.documentElement

import json
k1data=json.loads(collection.firstChild.data)
print(int(k1data['Key'][0]['TBROW']))
for ii in range(int(k1data['Key'][0]['TBROW'])):
 print(str(k1data['ds'][ii]['NOM_ROLL_WIDTH']))

import pandas as pd
df=pd.read_json(json.dumps(k1data['ds']))
df
df['NOM_ROLL_THICK'].plot()
import matplotlib.pyplot as plt
plt.show()