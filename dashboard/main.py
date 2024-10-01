import streamlit as st
import pandas as pd
from function import *
import numpy as np

day_df = pd.read_csv("day_df_new.csv")
hour_df = pd.read_csv("hour_df_new.csv")

total_user2011 = day_df.groupby(by='year').agg({'total_user' : 'sum'}).loc[2011,'total_user']
total_user2012 = day_df.groupby(by='year').agg({'total_user' : 'sum'}).loc[2012,'total_user']

avg_temp2011 = day_df.groupby(by='year').agg({'temperature' : 'mean'}).loc[2011,'temperature']
avg_temp2012 = day_df.groupby(by='year').agg({'temperature' : 'mean'}).loc[2012,'temperature']

with st.sidebar:
    st.image('bike.jpg')
    selected_options = st.multiselect(
        'Pilih Tahun :',
        ['2011','2012'],
        default=['2011','2012']
    )

st.header('Bike Sharing Dataset Analysis')
st.subheader('Latar Belakang Dataset')
st.write('Dataset ini berisi data harian dan jam-jam tertentu mengenai penggunaan layanan bike-sharing selama dua tahun, yaitu 2011 dan 2012. Informasi yang tercakup meliputi tanggal, musim, tahun, bulan, serta hari dalam seminggu. Selain itu, terdapat indikator apakah suatu hari merupakan hari libur atau hari kerja, serta kondisi cuaca mulai dari cerah hingga hujan atau salju lebat. Data suhu, kelembaban, dan kecepatan angin juga dicatat, bersama dengan jumlah pengguna kasual dan terdaftar. Dataset ini memungkinkan analisis mendalam mengenai tren penggunaan bike-sharing berdasarkan faktor waktu dan cuaca, sehingga dapat memberikan wawasan mengenai pola penggunaan sepeda di berbagai kondisi.')
col1, col2 = st.columns(2)

with col1:
    if '2011' in selected_options and '2012' in selected_options:
        st.metric(label="Total User in 2011 & 2012", value=total_user2012+total_user2011)
    elif '2011' in selected_options:
        st.metric(label="Total User in 2011", value=total_user2011)
    elif '2012' in selected_options:
        st.metric(label="Total User in 2012", value=total_user2012, delta=str(total_user2012-total_user2011)+" from 2011")
with col2:
    if '2011' in selected_options and '2012' in selected_options:
        st.metric(label="Average Temperature in 2011 & 2012", value=str(round((avg_temp2011+avg_temp2012)/2,2)) + " °C")
    elif '2011' in selected_options:
        st.metric(label="Average Temperature in 2012", value=str(round(avg_temp2011,2)) + " °C")
    elif '2012' in selected_options:
        st.metric(label="Average Temperature in 2012", value=str(round(avg_temp2012,2))+" °C", delta=str(round(avg_temp2012-avg_temp2011,2))+ " °C from 2011")


if '2011' in selected_options and '2012' in selected_options:
    monthly_counts = hour_df.groupby(by=["month", "year"]).agg({
        "total_user": "sum"
        })
    linePlot(monthly_counts,'month','total_user','year','Year comparison')
elif '2011' in selected_options:
    monthly_counts = hour_df.groupby(by=["month", "year"]).agg({
        "total_user": "sum"
        })
    filtered_data = monthly_counts.loc[monthly_counts.index.get_level_values('year').isin([2011])]
    linePlot(filtered_data,'month','total_user','year','Total renters per month in 2011','husl')

elif '2012' in selected_options:
    monthly_counts = hour_df.groupby(by=["month", "year"]).agg({
        "total_user": "sum"
        })
    filtered_data = monthly_counts.loc[monthly_counts.index.get_level_values('year').isin([2012])]
    linePlot(filtered_data,'month','total_user','year','Total renters per month in 2012','husl')

barChart(hour_df,'season','total_user','season','Set2','The Effect of Seasonality on the Use of Bicycle Services','Musim','Total Rental')