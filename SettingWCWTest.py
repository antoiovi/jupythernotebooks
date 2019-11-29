import pandas as pd
import numpy as np 
dict = {'data': ['2019/01/29','2019/01/30','2019/01/31','2019/02/01']}
df=pd.DataFrame(dict)
df['data']=pd.to_datetime(df['data'],format='%Y/%m/%d')
strdata=pd.to_datetime(df['data']).dt.strftime('%d/%m/%Y')
df['data'] = pd.to_datetime(df['data']).dt.strftime('%d/%m/%Y')
df3=pd.DataFrame(dict)
f3=pd.DataFrame(dict)
df3['data']=pd.to_datetime(df3['data'],format='%Y/%m/%d')
x= pd.to_datetime(df3['data']).dt.strftime('%d/%m/%Y',)
df3.loc[:,'data'] =x
print(df3)