import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title='Bike Sharing Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)

# Load dataset
df = pd.read_csv('day.csv')

# Mengganti tipe data kolom dteday
df['dteday'] = pd.to_datetime(df['dteday'])

# Format angka agar lebih rapi tanpa koma untuk analisis
min_date = df['dteday'].min()
max_date = df['dteday'].max()

# Sidebar Filters
st.sidebar.header('Please Filter Here:')
start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu', min_value=min_date,
    max_value=max_date, value=[min_date, max_date]
)

# Filter the dataframe
main_df = df[(df['dteday'] >= pd.Timestamp(start_date)) &
             (df['dteday'] <= pd.Timestamp(end_date))]

# Main Page
st.title(':bar_chart: Bike Sharing Dashboard')
st.markdown('##')

# TOP Metrics
total_cnt = main_df['cnt'].sum()
total_registered = main_df['registered'].sum()
total_casual = main_df['casual'].sum()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Bike Sharing')
    st.subheader(f'{total_cnt:,}')
with middle_column:
    st.subheader('Total Member')
    st.subheader(f'{total_registered:,}')
with right_column:
    st.subheader('Total Non-Member')
    st.subheader(f'{total_casual:,}')

st.markdown('---')

if not main_df.empty:
    # Plot tren jumlah peminjaman sepeda sepanjang tahun 2011
    ddf_2011 = main_df[main_df['dteday'].dt.year == 2011]
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(ddf_2011['dteday'], ddf_2011['cnt'], marker='o', linestyle='-', color='b', alpha=0.6)
    ax1.set_xlabel('Bulan')
    ax1.set_ylabel('Total Peminjaman Sepeda')
    ax1.set_title('Tren Peminjaman Sepeda Harian - Tahun 2011')
    ax1.grid(True)
    st.pyplot(fig1)

    # Visualisasi rata-rata peminjaman berdasarkan cuaca
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(x='weathersit', y='cnt', data=main_df, palette='coolwarm', ax=ax2)
    ax2.set_xlabel('Cuaca')
    ax2.set_ylabel('Rata-rata Peminjaman Sepeda')
    ax2.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Cuaca')
    ax2.set_xticklabels(['Cerah', 'Mendung', 'Hujan'])
    st.pyplot(fig2)

    # Agregasi berdasarkan hari kerja
    ddf_holiday = main_df.groupby('workingday')['cnt'].mean()
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ddf_holiday.plot(kind='bar', color=['blue', 'red'], ax=ax3)
    ax3.set_xticklabels(['Hari Bukan Kerja', 'Hari Kerja'], rotation=0)
    ax3.set_xlabel('Kategori Hari')
    ax3.set_ylabel('Rata-rata Peminjaman')
    ax3.set_title('Perbandingan Peminjaman Sepeda pada Hari Kerja vs Hari Bukan Kerja')
    st.pyplot(fig3)
else:
    st.write('No data available for the selected filters.')

# Hide streamlit style
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
