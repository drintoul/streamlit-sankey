#!/usr/bin/env python
# coding: utf-8

# %pip install streamlit-jupyter

# In[24]:


get_ipython().run_line_magic('pip', 'install streamlit')


# In[25]:


import streamlit as st

#from streamlit_jupyter import StreamlitPatcher, tqdm

#StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers


# In[26]:


import yfinance as yf
import streamlit as st
import pandas as pd


# In[12]:


st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")


# In[22]:


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2023-12-11', end='2023-12-12')


# In[23]:


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




