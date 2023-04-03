import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats
from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M')
import plotly.express as px
import plotly.graph_objects as go
from mpl_toolkits import mplot3d
df = pd.read_csv('D:/OneDrive - Hanoi University of Science and Technology/Me/Code/DatainHUST/Code mẫu/t345678.csv',
                encoding="utf-8-sig",
                header=0,
                infer_datetime_format=True,
                parse_dates={'datetime':[0]},
                index_col=['datetime']
                )
df['time'] = df.index
df.loc[:,'month'] = pd.Series(df.index.month, df.index)
df.loc[:,'day'] = pd.Series(df.index.day, df.index)
df.loc[:,'hour'] = pd.Series(df.index.hour, df.index)
df.loc[:,'dayofweek'] = pd.Series(df.index.dayofweek, df.index)
df.loc[:,'dayname'] = pd.Series(df.index.day_name(), df.index)
df.loc[:,'hourofweek'] = pd.Series((df.hour+24*df.dayofweek), df.index)
df.loc[:,'hourofmonth'] = pd.Series((df.hour+24*(df.day-1)), df.index)
df.loc[:,'Tcell']=pd.Series((df['Ambient temperature(℃)']+df['Irradiance(W/㎡)']/800*(25-20)), df.index)
df.loc[:,'Pm']=pd.Series((2.172*1.303*220*2*590*df['Irradiance(W/㎡)']/1000*(1-0.0045*(df['Tcell']-25))*df['Inverter efficiency(%)']/100*(98-0.55*5/12)/100*20.1/100), df.index)
df.loc[:,'Hieu suat']=pd.Series((df['Total input power(kW)']*1000/df['Pm']*100), df.index)
x=[]
y=[]
z=[]
n=11
tuan=1
for i in range(len(df['time'])):
    if df['dayofweek'][i]>df['dayofweek'][i+1]:
        tuan=tuan+1
    if tuan==n:
        break
i=i+1
ax = plt.axes(projection='3d')
hieusuat=[]
while df['dayofweek'][i]<=df['dayofweek'][i+1]:
    if df['Hieu suat'][i]<100:
        hieusuat.append(df['Hieu suat'][i])
        x.append(df['Ambient temperature(℃)'][i])
        y.append(df['Irradiance(W/㎡)'][i])
        z.append(df['Hieu suat'][i])
    if (df['dayofweek'][i] != df['dayofweek'][i+1]):
        ax.scatter(x, y, z,s=2)
        x=[]
        y=[]
        z=[]  
    i=i+1

plt.xlabel('nhiet do')
plt.ylabel('buc xa')
ax.set_zlabel('hieu suat')
ax.set_title('theo tuan')
plt.show()
print(hieusuat)
plt.plot(hieusuat)
plt.show()