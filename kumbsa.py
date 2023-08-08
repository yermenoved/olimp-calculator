import pandas as pd
import matplotlib.pyplot as plt
from numpy import std

df = pd.read_excel('kumbsa.xlsx')
df.index = df['Дата']
df = df.drop(columns='Дата').T
dates = [i.split()[0]+' '+i.split()[1][-2:] for i in df.index]
df.index = dates

itogo = df['Итого по Столбцам'].to_frame()
itogo['SMA'] = itogo['Итого по Столбцам'].rolling(3).mean()

year_dividers = ['Январь '+str(i) for i in range(21, 24)]
plt.plot(itogo)
plt.xticks(rotation=90)
plt.vlines(year_dividers, 0, 2500, 'red', 'dotted')
plt.show()

years = {}
years[2021] = itogo.iloc[8:20, 0]
years[2022] = itogo.iloc[20:32, 0]

sums = {}
for year in years:
    sums[year] = sum(years[year])

coefs = {}
for year in years:
    coef = []
    for i in years[year]:
        coef.append(i/sums[year])
    coefs[year] = coef

coefs = pd.DataFrame(coefs)

avg = []
stdev = []
for i in range(12):
    avg.append(coefs.loc[i,:].mean())
    stdev.append(std(coefs.loc[i,:]))
coefs['avg'] = avg
coefs['stdev'] = stdev

coefs.to_csv('kumbsa_coefs.csv')
# Conclusion: too high stdev makes impossible to conclude anything from the sample