import streamlit as st
import numpy as np
import numpy_financial as npf
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import requests
import json
import altair as alt
import yfinance as yf
import fredapi
from fredapi import Fred
import datetime as dt
import pydeck as pdk
import statsmodels.api as sm
import nasdaqdatalink
#KtkauE_-pic1EFrCBFb4
from sec_edgar_downloader import Downloader


#Home Page

# Sidebar dropdown 
option = st.sidebar.selectbox("Dashboard", ('Home', 'Valuation Models', 'Performance', 'SEC Document Analysis', 'Comparison Analysis', 'Framework')) 

#Title & Header
if option == 'Home':
    st.title("Collin Jones")
    st.header("Data Analytics In Finance")
    st.text("Final Project")
    st.text("  Navigation With Left Dashboard | Framework & Source Code On 'Framework' Page")
    st.text(" ")
    st.markdown("""---""")
    st.text(" ")
    st.text(" Index | Valuations Models, Performance Visualization Models, SEC Document Analysis, Comparison Analysis, Framework")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    #weather
    api_key = "54c08ecafc87e0166d56037c1fdaa23a"
    lat = "41.8786"
    lon = "-87.6251"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    current = data["current"]["temp"]
    w = data["current"]["wind_speed"]
    h = data["current"]["humidity"]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", current, "1.2 °F")
    col2.metric("Wind", w, "3mph")
    col3.metric("Humidity", h, "4%")
   
 
    #map
    st.pydeck_chart(pdk.Deck(
         map_style='mapbox://styles/mapbox/dark-v8',
         initial_view_state=pdk.ViewState(
         latitude=41.87,
         longitude=-87.62,
         zoom=11,
         pitch=50)))
 
 

#pages

if option == 'Valuation Models':
    st.header("Valuation Models")
    
if option == 'Performance':
    st.header("Economic Indicator Correlation Matrix")

if option == 'SEC Document Analysis':
    st.header("SEC EDGAR API")
    
if option == 'Comparison Analysis':
    st.header("Digital Assets")
    
    

if option == 'Framework':
    st.subheader("Framework")


    
    
    
    
    

#Page 2

if option == 'Valuation Models':
    st.markdown("""---""")
    st.text("")
    st.subheader('Capital Asset Pricing Model')
    
    
    
    
    
    
    
    
    
    
    st.markdown("""---""")
    st.subheader("Simple Discounted Cash Flow Analysis")
    st.text("")
    
    st.text("Projcted Yearly Free Cash Flow")
    a0, a1, a2, = st.columns(3)
    a3, a4, a5, = st.columns(3)
    y0 = a0.number_input('Initial Investment', None, None, 100)
    y1 = a1.number_input('Year 1', None, None, 10)
    y2 = a2.number_input('Year 2', None, None, 20)
    y3 = a3.number_input('Year 3', None, None, 30)
    y4 = a4.number_input('Year 4', None, None, 40)
    y5 = a5.number_input('Year 5', None, None, 50)
    r = st.slider('Discount Rate %', 0, 100, 20)
    
    fv = y0 + y1 + y2 + y3 + y4 + y5
    pv = -y0 + y1/(1+r/100)**1 + y2/(1+r/100)**2 + y3/(1+r/100)**3 + y4/(1+r/100)**4 + y5/(1+r/100)**5
    ir = npf.irr([-y0, y1, y2, y3, y4, y5])
    irr = ir * 100
   
    st.write('Net Present Value', pv)
    st.write('Internal Rate of Return', irr)
    
    
 
    
    
                    
           
    

    

#Page 3

if option == 'Performance' :
    st.markdown("""---""")
    st.text("")
    
    fred = Fred(api_key='49dc69fb7e224d27e8cd2f5b4830ac9f')
    nasdaqdatalink.ApiConfig.api_key = "KtkauE_-pic1EFrCBFb4"
    start = pd.to_datetime('2010-01-01')
    end = pd.to_datetime('today')
    

    two = fred.get_series('DGS2', observation_start=start, observation_end=end)
    two.name = 'Two Year'
    five = fred.get_series('DGS5', observation_start=start, observation_end=end)
    five.name = 'Five Year'
    ten = fred.get_series('T10Y2Y', observation_start=start, observation_end=end)
    ten.name = 'Ten Year'
    
    gdp = fred.get_series('GDPC1', start, end)
    gdp.name = 'Real Gross Domestic Product'
    cir = fred.get_series('WCURCIR', start, end)
    cir.name = 'Currency in Circulation'
    un = fred.get_series('UNRATE', start, end)
    un.name = 'Unemployment'
    cpi = fred.get_series('CPGRLE01ISQ659N', start, end)
    cpi.name = 'Consumer Price Index'
    
    gdpcpi = pd.merge(gdp, un, left_index = True, right_index = True)
    econ = pd.merge(cir, cpi, left_index = True, right_index = True)
    
    
    
    st.text('Gross Domestic Product') 
    st.line_chart(gdpcpi)
    st.write(gdpcpi.tail())   
    
    
    st.markdown("""---""")
   
    
    st.text('Currency in Circulation | Unemployment')
    st.area_chart(econ)
    st.write(econ)
    
   
   
 
    
    
    
  
    

    



#Page 4

if option == 'SEC Document Analysis' :
    st.markdown('''# Wall St.
    ''')
    
    from sec_edgar_downloader import Downloader
    dl = Downloader("/Users/quoc/Downloads/")
    
    tik = st.text_input('Company Ticker', 'AAPL')
    
    
    tenk = dl.get("10-K", 'tik', amount=5)
    dl.get("10-Q", 'tik', amount=40)
    dl.get("8-K", 'tik', amount=5)
    
    st.write(tenk)
    
    
    start = pd.to_datetime('2018-01-01')
    end = pd.to_datetime('today')
    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret
    
    
    
    
    stock = yf.Ticker(tik)
    
    st.write('Quarterly Financials')
    qf = pd.DataFrame(stock.quarterly_financials)
    qf.dropna(inplace=True)
    st.write(qf)

    
    st.write('Largest Share Holders')
    stock.major_holders
   
    

   

    







#Page 5

if option == 'Comparison Analysis' :
    st.text("Data")
    
    tickers = ('VTI', 'SPY', 'DIA', 'GME', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD')

    dropdown = st.multiselect('assets', tickers)

    start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret

    if len(dropdown) > 0:
     #df = yf.download(dropdown,start,end) ['Adj Close'] 
        df = relativeret(yf.download(dropdown,start,end) ['Adj Close'])
   
        st.area_chart(df)
    
    
    #Framework Page
    
if option == 'Framework' :
     st.text("Framework & Source Code")
     st.markdown("""---""")
    
    
     st.subheader('https://github.com/01Jones/CJ/edit/main/CJ.py')
      
     st.text(" ")
     st.markdown("""---""")

 
        
