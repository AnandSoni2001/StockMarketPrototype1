#Import Libraries
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from yahoo_fin import stock_info

#Heading
st.title('Research Project on Stock Market Analysis and Prediction')
st.write("#")

#TCS Data Taken
tcsdaily = stock_info.get_data("TCS.NS", interval="1d")
tcsmonthly= stock_info.get_data("TCS.NS", interval="1mo")
tcsyearly = pd.read_csv('data/tcs-yearly.csv')

#Reliance Data Taken
reldaily = stock_info.get_data("RELIANCE.NS", interval="1d")
relmonthly= stock_info.get_data("RELIANCE.NS", interval="1mo")
relyearly = pd.read_csv('data/relianceind-yearly.csv')

#Infosys Data Taken
infdaily = stock_info.get_data("INFY.NS", interval="1d")
infmonthly= stock_info.get_data("INFY.NS", interval="1mo")
infyearly = pd.read_csv('data/infosys-yearly.csv')

#Select Box
comp = st.selectbox('Select a Company from the below options :', ('Tata Consultancy Services', 'Reliance Industries', 'Infosys'))

if comp == 'Tata Consultancy Services':
    col1, col2, col3, col4 = st.columns(4)
    x = round(stock_info.get_live_price("TCS.NS"),2)
    y = round(tcsdaily['close'].iloc[-2],2)
    col1.metric(label="Market Price", value=x, delta = round(x-y,2))
    col2.metric(label="52 Week Low", value=round(tcsdaily['low'].tail(261).min(),2))
    col3.metric(label="52 Week High", value=round(tcsdaily['high'].tail(261).max(),2))
    col4.metric(label='Previous Close', value=y)


if comp == 'Reliance Industries':
    col1, col2, col3, col4 = st.columns(4)
    x = round(stock_info.get_live_price("RELIANCE.NS"),2)
    y = round(reldaily['close'].iloc[-2],2)
    col1.metric(label="Market Price", value=x, delta = round(x-y,2))
    col2.metric(label="52 Week Low", value=round(reldaily['low'].tail(261).min(),2))
    col3.metric(label="52 Week High", value=round(reldaily['high'].tail(261).max(),2))
    col4.metric(label='Previous Close', value=y)

if comp == 'Infosys':
    col1, col2, col3, col4 = st.columns(4)
    x = round(stock_info.get_live_price("INFY.NS"),2)
    y = round(infdaily['close'].iloc[-2],2)
    col1.metric(label="Market Price", value=x, delta = round(x-y,2))
    col2.metric(label="52 Week Low", value=round(infdaily['low'].tail(261).min(),2))
    col3.metric(label="52 Week High", value=round(infdaily['high'].tail(261).max(),2))
    col4.metric(label='Previous Close', value=y)

#Tab for Hist Data
st.write("#")
st.subheader('Historic data : ')
option1, option2, option3 = st.tabs(["Daily", "Monthly", "Yearly"])

cl1, cl2, cl3, cl4 = st.columns(4)
with cl1:
    ag1 = st.checkbox('Close', value='True')
with cl2:
    ag2 = st.checkbox('Open', value='True')
with cl3:
    ag3 = st.checkbox('High', value='True')
with cl4:
    ag4 = st.checkbox('Low', value='True')
            
with option1:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsdaily, y='close',markers=False, title='Tata Consultancy Services Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)
        
        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(y=tcsdaily['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=tcsdaily['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=tcsdaily['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=tcsdaily['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters along close')
        st.plotly_chart(fig, use_container_width=True, title='Comparing other relevant parameters')

    if comp == 'Infosys':
        fig = px.line(infdaily, y='close',markers=False, title='Infosys Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()   
        if(ag1):
            fig.add_trace(go.Scatter(y=infdaily['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=infdaily['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=infdaily['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=infdaily['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(reldaily, y='close',markers=False, title='Reliance Industries Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(y=reldaily['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=reldaily['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=reldaily['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=reldaily['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters along close')
        st.plotly_chart(fig, use_container_width=True)

with option2:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsmonthly,y='close', markers=False, title='Tata Consultancy Services Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(y=tcsmonthly['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=tcsmonthly['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=tcsmonthly['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=tcsmonthly['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Infosys':
        fig = px.line(infmonthly, y='close',markers=False, title='Infosys Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(y=infmonthly['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=infmonthly['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=infmonthly['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=infmonthly['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(relmonthly, y='close',markers=False, title='Reliance Industries Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(y=relmonthly['close'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(y=relmonthly['open'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(y=relmonthly['high'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(y=relmonthly['low'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

with option3:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsyearly, x='Year', y='Close Price',markers=False, title='Tata Consultancy Services Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)
        
        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Close Price'], name='Closing', line=dict(color='blue')))
        if(ag1):
            fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Open Price'], name = 'Opening', line=dict(color='yellow')))
        if(ag1):
            fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['High Price'], name = 'High', line=dict(color='green')))
        if(ag1):
            fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters along close price')
        st.plotly_chart(fig, use_container_width=True, title='Comparing other relevant parameters')

    if comp == 'Infosys':
        fig = px.line(infyearly, x='Year', y='Close Price',markers=True, title='Infosys Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Close Price'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Open Price'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['High Price'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(relyearly, x='Year', y='Close Price',markers=True, title='Reliance Industries Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        if(ag1):
            fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Close Price'], name='Closing', line=dict(color='blue')))
        if(ag2):
            fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Open Price'], name = 'Opening', line=dict(color='yellow')))
        if(ag3):
            fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['High Price'], name = 'High', line=dict(color='green')))
        if(ag4):
            fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

#Tab for Hist Data
st.write("#")
st.subheader('Financial data : ')
a1, a2, a3 = st.tabs(["Revenue & Profit", "Net Worth", "Shareholding Pattern"])

tier=['Promoters', 'Mutual Funds', 'Retail', 'Foreign Institutions','Others'] 
y=['2018', '2019', '2020', '2021', '2022']

with a1:
    st.caption('All values in Crs')
    if comp == 'Infosys':
        chart_data = pd.DataFrame([[70522,16029], [82675,15404], [90791,16594], [100472,19351], [121641,22110]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    if comp == 'Tata Consultancy Services':
        chart_data = pd.DataFrame([[123104,25826], [146463,31472], [156949,32430], [164177,32430], [191754,38327]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    if comp == 'Reliance Industries':
        chart_data = pd.DataFrame([[408265,36075], [583094,39588], [611645,39354], [486326,49128], [721634,60705]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    
with a2:
    st.caption('All values in Crs')
    if comp == 'Infosys':
        chart_data = pd.DataFrame([64923, 64948, 65450, 76351, 75350], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

    if comp == 'Tata Consultancy Services':
        chart_data = pd.DataFrame([85128, 89446, 84126, 86433, 89139], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

    if comp == 'Reliance Industries':
        chart_data = pd.DataFrame([293506, 387112, 453331, 700172, 779485], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

with a3:
    if comp == 'Infosys':
        x = [15.11, 17.71, 18.22, 36.28, 12.68]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

    if comp == 'Tata Consultancy Services':
        x = [72.30, 3.31, 5.96, 12.94, 5.49]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

    if comp == 'Reliance Industries':
        x = [50.49, 5.81, 11.64, 23.43, 8.63]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

st.caption('This webapp was made by Anand Soni and Deepak Rathore.')
