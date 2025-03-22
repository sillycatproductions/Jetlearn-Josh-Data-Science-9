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
fig2 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h', color_continuous_scale = ['green','red'], title = 'Top 10 Death Cases Countries')
fig2.write_html('Fig2.html', auto_open = True)

top10_recovered = pd.DataFrame(data.groupby('Country')['Recovered'].sum().nlargest(10).sort_values(ascending = False))
fig3 = px.scatter(top10_recovered,x = top10_recovered.index, y = 'Recovered', size ='Recovered', size_max = 120, color = top10_recovered.index, title = 'Top 10 Countries with the most Recovered People')
fig3.write_html('Fig3.html', auto_open = True)

top10_active = pd.DataFrame(data.groupby('Country')['Active'].sum().nlargest(10).sort_values(ascending = False))
fig4 = px.bar(top10_active, x = 'Active', y = top10_active.index, height = 600, color = 'Active', orientation = 'h', color_continuous_scale = ['green','red'], title = 'Top 10 Active Cases in Countries')
fig4.write_html('Fig4.html', auto_open = True)

topstates_us = data['Country'] == 'US'
topstates_us = data[topstates_us].nlargest(5, 'Confirmed')

afig1 = go.Figure(data = [go.Bar(name = 'Confirmed Cases', x = topstates_us['Confirmed'], y = topstates_us['Confirmed'], orientation = 'h')])
afig1.update_layout(title = 'Most confirmed cases in USA', height = 600)
afig1.write_html('AFig1.html', auto_open = True)

topstates_uk = data['Country'] == 'United Kingdom'
topstates_uk = data[topstates_uk].nlargest(5, 'Recovered')

afig2 = go.Figure(data = [go.Bar(name = 'Confirmed Cases', x = topstates_uk['Recovered'], y = topstates_uk['Recovered'], orientation = 'h')])
afig2.update_layout(title = 'Most recovered cases in United Kingdom', height = 600)
afig2.write_html('AFig2.html', auto_open = True)
