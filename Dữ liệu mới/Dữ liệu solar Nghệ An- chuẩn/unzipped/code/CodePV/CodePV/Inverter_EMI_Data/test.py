df2.loc[:,'hstt']=pd.Series((df2['stt']*b[1]+b[0]), df.index)
df2.loc[:,'saiso']=pd.Series(((df2['Hieu suat']-df2['hstt'])/df2['hstt']), df.index)
df2=df2[abs(df2['saiso'])<=0.01]
df2.head()