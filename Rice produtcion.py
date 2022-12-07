#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
Rice = pd.read_csv('/Users/kyuripark/Downloads/Rice Production.csv' ,  encoding='cp949')
Rice


# In[2]:


Rice = Rice [['2010','2011','2012', '2013', '2014', '2015','2016','2017','2018','2019','2020']]


# In[18]:


IndiaRice= Rice.loc[2]
IndiaRice= pd.DataFrame(IndiaRice)
IndiaRice.columns = ['Rice']
IndiaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
IndiaRice['Rice'] = IndiaRice['Rice'].astype(int)

import matplotlib.pyplot as plt

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= IndiaRice['Rice']

## 시각화
plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Rice_production, color='blue',label= 'M/T')
plt.legend(loc=2)
plt.title('2010-2020 India Rice Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v, Rice_production[i],  Rice_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

    
    
plt.show()


# In[19]:


ChinaRice= Rice.loc[1]
ChinaRice = pd.DataFrame(ChinaRice)
ChinaRice.columns = ['Rice']
ChinaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
ChinaRice['Rice'] = ChinaRice['Rice'].astype(int)

import matplotlib.pyplot as plt

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= ChinaRice['Rice']

## 시각화
plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Rice_production, color='blue',label= 'M/T')
plt.legend(loc=2)
plt.title('2010-2020 China Rice Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v, Rice_production[i],  Rice_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.show()


# In[20]:


IndonesiaRice= Rice.loc[3]
IndonesiaRice = pd.DataFrame(IndonesiaRice)
IndonesiaRice.columns = ['Rice']
IndonesiaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
IndonesiaRice['Rice'] = IndonesiaRice['Rice'].astype(int)

import matplotlib.pyplot as plt

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= IndonesiaRice['Rice']

## 시각화
plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Rice_production, color='blue',label= 'M/T')
plt.legend(loc=2)

plt.title('2010-2020 Indonesia Rice Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v, Rice_production[i],  Rice_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)



plt.show()

