import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Rice production')
st.write('India Rice Production')

Rice = pd.read_csv('/Users/kyuripark/Downloads/Rice Production.csv' ,  encoding='cp949')
Rice = Rice [['2010','2011','2012', '2013', '2014', '2015','2016','2017','2018','2019','2020']]
IndiaRice= Rice.loc[2]
IndiaRice= pd.DataFrame(IndiaRice)
IndiaRice.columns = ['Rice']
IndiaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
IndiaRice['Rice'] = IndiaRice['Rice'].astype(int)

st.dataframe(IndiaRice)


## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= IndiaRice['Rice']

## 시각화
fig1 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
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

 
st.pyplot(fig1)


st.write('China Rice Production')
ChinaRice= Rice.loc[1]
ChinaRice = pd.DataFrame(ChinaRice)
ChinaRice.columns = ['Rice']
ChinaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
ChinaRice['Rice'] = ChinaRice['Rice'].astype(int)
st.dataframe(ChinaRice)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= ChinaRice['Rice']

## 시각화
fig2 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
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

st.pyplot(fig2)


st.write('Indonesia Rice Production')
IndonesiaRice= Rice.loc[3]
IndonesiaRice = pd.DataFrame(IndonesiaRice)
IndonesiaRice.columns = ['Rice']
IndonesiaRice.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
IndonesiaRice['Rice'] = IndonesiaRice['Rice'].astype(int)
st.dataframe(IndonesiaRice)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Rice_production= IndonesiaRice['Rice']

## 시각화
fig3 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
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

st.pyplot(fig3)

st.title('Maize production')
st.write('US Maize Production')
#옥수수 밀
Maize_Wheat = pd.read_csv('/Users/kyuripark/Downloads/농업생산량_밀__옥수수__20221205090501.csv',  encoding='cp949')
Maize = Maize_Wheat[['2010.2','2011.2','2012.2', '2013.2', '2014.2', '2015.2','2016.2','2017.2','2018.2','2019.2','2020.2']]
US_Maize= Maize.loc[3]
US_Maize = pd.DataFrame(US_Maize)
US_Maize.columns = ['Maize']
US_Maize.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
US_Maize['Maize'] = US_Maize['Maize'].astype(int)
st.dataframe(US_Maize)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Maize_production= US_Maize['Maize']

## 시각화
fig4 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Maize_production, color='green', label= 'M/T')
plt.legend(loc=0) 
plt.title('2010-2020 U.S. Maize Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v,Maize_production[i], Maize_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

st.pyplot(fig4)

st.write('China Maize Production')
ChinaMaize = Maize.loc[1]
ChinaMaize= pd.DataFrame(ChinaMaize)
ChinaMaize = pd.DataFrame(ChinaMaize)
ChinaMaize.columns = ['Maize']
ChinaMaize.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
ChinaMaize['Maize'] =ChinaMaize['Maize'].astype(int)
st.dataframe(ChinaMaize)

year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Maize_production= ChinaMaize['Maize']

## 시각화
fig5 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Maize_production, color='green',label= 'M/T')
plt.legend(loc=0) 
plt.title('2010-2020 China Maize Production ',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v,Maize_production[i], Maize_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)
    

st.pyplot(fig5)

st.write('Brazil Maize Production')
BrazilMaize = Maize.loc[4]
BrazilMaize = pd.DataFrame(BrazilMaize)
BrazilMaize.columns = ['Maize']
BrazilMaize.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
BrazilMaize['Maize'] = BrazilMaize['Maize'].astype(int)
st.dataframe(BrazilMaize)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Maize_production= BrazilMaize['Maize']

## 시각화
fig6 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Maize_production, color='green',label= 'M/T')
plt.legend(loc=2) 
plt.title('2010-2020 Brazil Maize Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v,Maize_production[i], Maize_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

st.pyplot(fig6)

st.title('Wheat Production')
st.write('India Wheat Production')
Wheat = Maize_Wheat [['2010','2011','2012', '2013', '2014', '2015','2016','2017','2018','2019','2020']]
India_Wheat= Wheat.loc[2]
India_Wheat = pd.DataFrame(India_Wheat)
India_Wheat.columns = ['Wheat']
India_Wheat.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
India_Wheat['Wheat'] = India_Wheat['Wheat'].astype(int)
st.dataframe(India_Wheat)
## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Wheat_production= India_Wheat['Wheat']
fig7 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Wheat_production, color='orange',label= 'M/T')
plt.legend(loc=2) 
plt.title('2010-2020 India Wheat Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 


for i, v in enumerate(xtick_label_position):
    plt.text(v, Wheat_production[i],  Wheat_production[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 8, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

st.pyplot(fig7)

st.write('China Wheat Production')

China_Wheat= Wheat.loc[1]
China_Wheat = pd.DataFrame(China_Wheat)
China_Wheat.columns = ['Wheat']
China_Wheat.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
China_Wheat['Wheat'] = China_Wheat['Wheat'].astype(int)
st.dataframe(China_Wheat)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Wheat_production= China_Wheat['Wheat']

## 시각화
fig8= plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Wheat_production, color='orange',label= 'M/T')
plt.legend(loc=2) 
plt.title('2010-2020 China Wheat Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
st.pyplot(fig8)


st.write('Russia Wheat Production')
Russia_Wheat= Wheat.loc[5]
Russia_Wheat = pd.DataFrame(Russia_Wheat)
Russia_Wheat.columns = ['Wheat']
Russia_Wheat.index=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
Russia_Wheat['Wheat'] = Russia_Wheat['Wheat'].astype(int)
st.dataframe(Russia_Wheat)

## 데이터
year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] 
Wheat_production= Russia_Wheat['Wheat']

## 시각화
fig9 = plt.figure(figsize=(10,10)) ## Figure 생성 사이즈는 10 by 10
xtick_label_position = list(range(len(year))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, year) ## x축 눈금 라벨 출력

plt.bar(xtick_label_position, Wheat_production, color='orange',label= 'M/T')
plt.legend(loc=2) 
plt.title('2010-2020 Russia Wheat Production',fontsize=20) ## 타이틀 출력
plt.xlabel('Year') ## x축 라벨 출력
plt.ylabel('Production') ## y축 라벨 출력 

for i, v in enumerate(xtick_label_position):
    plt.text(v, Wheat_production[i],  Wheat_production[i],      
    fontsize = 8, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

st.pyplot(fig9)
