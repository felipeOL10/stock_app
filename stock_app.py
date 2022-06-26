import streamlit as st
import pandas as pd 
import yfinance as yf
import cufflinks as cf

st.set_page_config(layout="wide")

st.markdown('''
# Stock Financials App

**Credits**
- App built by Felipe Lima
- Built in `Python` using `streamlit`,`yfinance` and `pandas`
''')

ticker = st.text_input("Pick your stock (INSERT IN CAPS):")

start_date = st.date_input('Start', value=pd.to_datetime('2018-01-01'))
end_date = st.date_input('End', value=pd.to_datetime('today'))

stock = yf.Ticker(ticker)
st.subheader("Stock recommendations")
d = stock.recommendations
st.dataframe(d)
st.subheader("Stock financials")
df = stock.financials
st.dataframe(df)
st.subheader("Stock Balance sheet")
df1 = stock.balance_sheet
st.dataframe(df)
st.subheader("Stock Cash Flow")
df2 = stock.cashflow
st.dataframe(df)
st.subheader("Stock Earnings")
df3 = stock.earnings
st.dataframe(df)
st.subheader("Stock Dividends")
df4 = stock.dividends
st.dataframe(df4)

st.header("Returns of closing prices")

def returns(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

price_data = returns(yf.download(ticker, start_date, end_date))['Adj Close']
st.line_chart(price_data)

# Bollinger bands
st.header('**Bollinger Bands**')
price = stock.history(period='1d', start=start_date, end= end_date)
qf=cf.QuantFig(price,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

st.info('Credit: Created by Felipe Lima')

