import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv('data.csv')
fig = px.line(df, x='cases', y='date', color='country', title='Covid cases in China')
fig.show()