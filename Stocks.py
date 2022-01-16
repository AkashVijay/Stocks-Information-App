import yfinance as yf
import streamlit as st
import pandas as pd

st.sidebar.subheader('Choose Company')
companyList = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
stock = st.sidebar.selectbox('', companyList) 

st.markdown("<h1 style='text-align: center; color: #50C878;'>Stock Information App</h1>", unsafe_allow_html=True)

tickerData = yf.Ticker(stock) 

tickerInfo = tickerData.info

st.header('**%s**' % tickerInfo['longName'])

st.markdown('<img src=%s>' % tickerInfo['logo_url'], unsafe_allow_html=True)


st.write("""## About""")
about = tickerInfo['longBusinessSummary']
st.info(about)

tickerDate= tickerData.history(period='1d', start='2010-1-11', end='2022-1-16')
st.write("""## Closing Price""")
st.line_chart(tickerDate.Close)
st.write("""## Volume Price""")
st.line_chart(tickerDate.Volume)

st.write("""## Calendar""")
tickerData._calendar
st.write("""## Major Holders""")
tickerData.major_holders
st.write("""## Recommendations""")
tickerData.recommendations
st.write("""## Financials""")
tickerData.financials