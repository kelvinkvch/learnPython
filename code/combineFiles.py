import pandas as pd
import os,glob
path=r'c:\Users\kelvi\Desktop\test'
files=glob.glob(os.path.join(path,'*.xls*'))
cols=['序号','姓名','班组','性别','联系电话','接触家属人数','未外出','省内外出地点','省内返回日期','省内返回交通工具','省内同行家属数','省外外出地','省外返回日期','省外返回交通工具','省外同行家属数','国外外出地','国外返回日期','国外返回交通工具','国外同行家属数','是否感染','家属感染数','是否疑似感染','疑似感染家属数','是否到过湖北或接触河北人','到过湖北的家属数','是否还在湖北','是否感冒伴疑似','是否只感冒','是否已解除隔离','其他']
dft=[]
for file in files:    
    df=pd.read_excel(file,skiprows=5,header=None)
    df.columns=cols
    df.drop(df.index[-2:],axis=0,inplace=True)
    dft.append(df)
    # print(df)
dff=pd.concat(dft,ignore_index=True)
# print(len(cols))
dff.to_csv('test.csv',index=False)