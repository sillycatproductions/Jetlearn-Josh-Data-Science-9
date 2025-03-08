import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv('covid_data.csv')
data = data[['Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Recovered','Deaths','Active']]

data.columns = ('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')
data['State'].fillna(value = ' ', inplace = True)

top10_confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
fig1 = px.scatter(top10_confirmed,x = top10_confirmed.index, y = 'Confirmed', size= 'Confirmed', size_max = 120, color = top10_confirmed.index, title = 'Top 10 Countries by Confirmed Cases')
fig1.write_html('Fig1.html', auto_open = True)

top10_deaths = pd.DataFrame(data.groupby('Country')['Deaths'].sum().nlargest(10).sort_values(ascending = False))
fig2 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h', color_continuous_scale = ['deepskyblue','red'], title = 'Top 10 Death Cases Countries')
fig2.write_html('Fig2.html', auto_open = True)