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

# Home Page

# Sidebar dropdown 
option = st.sidebar.selectbox("Dashboard", ('Home', 'Valuation Models', 'Performance', 'Digital Assets', 'Page 4', 'Framework')) 

#Title & Header
if option == 'Home':
    st.title("Collin Jones")
    st.header("Project")
    st.text(" ")
    st.text("  Navigation With Left Dashboard | Framework & Source Code On 'Framework' Page")
    st.text(" ")
    st.markdown("""---""")
    st.text(" ")
    st.text(" Index | Valuations Models, Performance Visualization Models, Digital Asset Tracker, Page 4, Framework")
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

if option == 'Digital Assets':
    st.header("Digital Assets")

if option == 'Framework':
    st.subheader("Framework")


    
    
    
    
    

#Page 2

if option == 'Valuation Models':
    st.markdown("""---""")
    st.text("")
    st.subheader('Capital Asset Pricing Model')
    
    
    
    
    
    
    
    
    
    
    st.markdown("""---""")
    st.subheader("Discounted Cash Flow Analysis")
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
    
   
    
    spy = yf.download('SPY',start,end) 
    
    
    

    two = fred.get_series('DGS2', observation_start=start, observation_end=end)
    five = fred.get_series('DGS5', observation_start=start, observation_end=end)
    ten = fred.get_series('T10Y2Y', observation_start=start, observation_end=end)
    
    un = fred.get_series_as_of_date('UNRATE', end)
    gdp = pd.DataFrame(fred.get_series_as_of_date('GDP', end))
    
    #spy = nasdaqdatalink.get("SPY", start_date=start, end_date=end, returns="numpy")
    
    
    st.write(gdp)
    st.write(un)
    st.write(spy)
   
    st.altair_chart(gdp, use_container_width=True) 
    
   
    
    
    
   
    
        

    
    
    
    
    
        
     
    

    



#Page 4
if option == 'Digital Assets' :
    st.markdown('''# Crypto Currency
    ''')


    # Load market data from Binance API
    df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # Widget (Cryptocurrency selection box)
    col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('LINKBUSD') )
    col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('DOTBUSD') )
    col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
    col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
    col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
    col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('SOLBUSD') )
    col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]
    col2_df = df[df.symbol == col2_selection]
    col3_df = df[df.symbol == col3_selection]
    col4_df = df[df.symbol == col4_selection]
    col5_df = df[df.symbol == col5_selection]
    col6_df = df[df.symbol == col6_selection]
    col7_df = df[df.symbol == col7_selection]
    col8_df = df[df.symbol == col8_selection]
    col9_df = df[df.symbol == col9_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)
    col2_price = round_value(col2_df.weightedAvgPrice)
    col3_price = round_value(col3_df.weightedAvgPrice)
    col4_price = round_value(col4_df.weightedAvgPrice)
    col5_price = round_value(col5_df.weightedAvgPrice)
    col6_price = round_value(col6_df.weightedAvgPrice)
    col7_price = round_value(col7_df.weightedAvgPrice)
    col8_price = round_value(col8_df.weightedAvgPrice)
    col9_price = round_value(col9_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    col2_percent = f'{float(col2_df.priceChangePercent)}%'
    col3_percent = f'{float(col3_df.priceChangePercent)}%'
    col4_percent = f'{float(col4_df.priceChangePercent)}%'
    col5_percent = f'{float(col5_df.priceChangePercent)}%'
    col6_percent = f'{float(col6_df.priceChangePercent)}%'
    col7_percent = f'{float(col7_df.priceChangePercent)}%'
    col8_percent = f'{float(col8_df.priceChangePercent)}%'
    col9_percent = f'{float(col9_df.priceChangePercent)}%'

    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    col2.metric(col2_selection, col2_price, col2_percent)
    col3.metric(col3_selection, col3_price, col3_percent)
    col1.metric(col4_selection, col4_price, col4_percent)
    col2.metric(col5_selection, col5_price, col5_percent)
    col3.metric(col6_selection, col6_price, col6_percent)
    col1.metric(col7_selection, col7_price, col7_percent)
    col2.metric(col8_selection, col8_price, col8_percent)
    col3.metric(col9_selection, col9_price, col9_percent)

    st.header('**All Price**')
    st.dataframe(df)

    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)







#Page 5

if option == 'Page 4' :
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
     st.text("Data")
  
     st.echo(code_loction=above)
        
