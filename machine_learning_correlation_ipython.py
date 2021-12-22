import pickle
df = pickle.load('data__corr.pkl', 'rb')
df = pickle.load(open('data__corr.pkl', 'rb'))
df
df.columns
import pandas as pd
corln = df.corr()
df.columns
corln['New Positives']
corln['New Positives'].sort_values
corln['New Positives'].sort_values()
corln['New Positives'].sort_values(ascending=False)
df['population'] = df['pop_dens'] * df['area(sq mi)']
df.columns
corln = df.corr()
corln['New Positives'].sort_values(ascending=False)
from pandas.plotting import scatter_matrix
get_ipython().run_line_magic('clear', '')
corln['New Positives'].sort_values(ascending=False)
features = ['New Positives', 'Total Tests', 'population', 'highschool graduate', 'No Poverty', 'Median income']
df
scatter_matrix(df[features].iloc[0:62], figsize=(12,8))
import matplotlib.pyplot as plt
plt.show()
df.columns
df.iloc[0:62].plot(kind='scatter', x='New Positives', 'population']
df.iloc[0:62].plot(kind='scatter', x='New Positives', 'population')
df.iloc[0:62].plot(kind='scatter', x='New Positives', y='population')
df.iloc[0:62].plot(kind='scatter', x='New Positives', y=''No Poverty')
df.iloc[0:62].plot(kind='scatter', x='New Positives', y='No Poverty')
plt.show()
df.columns
df.iloc[0:62].plot(kind='scatter', x='Total Tests', y='Median income')
df.iloc[0:62].plot(kind='scatter', x='Total Tests', y='No Poverty')
plt.show()
df.iloc[0:62].plot(kind='scatter', x='New Positives, y='Median income')
df.iloc[0:62].plot(kind='scatter', x='New Positives', y='Median income')
plt.show()
