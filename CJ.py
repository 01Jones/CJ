import streamlit as st
import pandas as pd
import numpy as np
import requests
import yfinance as yf
import fredapi
import json



# Sidebar dropdown 
option = st.sidebar.selectbox("Dashboard", ('Home', 'Page 2', 'Page 3', 'Framework')) 

#Title & Header
if option == 'Home':
    st.title("Collin Jones")
    st.header("Portfolio")

#pages

st.image("https://unsplash.com/photos/doN0ZGtH6oQ")

if option == 'Page 2':
    st.subheader("page 2 title")

if option == 'Page 3':
    st.subheader("page 3 title")

if option == 'Framework':
    st.subheader("Framework")




#Page 2
if option == 'Page 2' :
    st.text("Correlation")
    
    tickers = ('VTI', 'SPY', 'BTC-USD', 'ETH-USD', 'AAPL', 'MSFT',)

    dropdown = st.multiselect('assets', tickers)

    start = st.date_input('Start', value = pd.to_datetime('2020-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret

    if len(dropdown) > 0:
     #df = yf.download(dropdown,start,end) ['Adj Close'] 
        df = relativeret(yf.download(dropdown,start,end) ['Adj Close'])
   
        st.line_chart(df)



#Page 3

if option == 'Page 3' :
    st.text("Data")
from fredapi import Fred
fred = Fred(api_key='49dc69fb7e224d27e8cd2f5b4830ac9f')

data = fred.get_series('SP500')

data = fred.get_series_latest_release('GDP')
data.tail()
