#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests


# In[2]:


df=pd.read_excel("https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls", sheet_name='Data 1', skiprows=2)


# In[3]:


df


# In[4]:


df.columns = ['Datum', 'Dollars pro Barrel']


# In[5]:


df


# In[6]:


df.info() # Datumsspalte checken, ob diese auch als Datum erkannt wird


# In[7]:


df=df.set_index('Datum')


# In[8]:


df_resampled=df.resample('M').mean() # wir berechnen den monatlichen Durchschnitt und benennen den Dataframe um


# In[9]:


df_resampled #Wir lassen uns den neuen Dataframe anzeigen


# In[11]:


df_resampled.to_csv('oelpreis.csv')

