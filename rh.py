import pandas as pd
import matplotlib.pyplot as plt
from numpy import std

df = pd.read_excel('rh.xlsx')

df.index = df['Дата']
df = df.drop(columns='Дата').T
dates = [i.split()[0]+' '+i.split()[1][-2:] for i in df.index]
df.index = dates

itogo = df['Итого по Столбцам'].to_frame()
itogo['SMA'] = itogo['Итого по Столбцам'].rolling(3).mean()

#------------Plot the kumbsa test graph (apparent seasonality)------------#
year_dividers = ['Январь '+str(i) for i in range(10, 24)]
plt.plot(itogo)
plt.xticks(fontsize='xx-small', rotation=90)
plt.vlines(year_dividers, 0, 25000, 'red', 'dotted')
plt.show()

#------------Calculate the seasonality coefficient------------#
years = {}
for i in range(9,23):
    years[2000+i] = itogo.iloc[5+(i-9)*12:17+(i-9)*12,0]

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

print(coefs)