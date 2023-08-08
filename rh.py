# Январь: 6,9+-1,9
# Февраль: 7,5+-1,8
# Март: 6,9+-1,1

# Апрель: 8,3+-1,4
# Май: 7,5+-0,8
# Июнь: 8,4+-0,6

# Июль: 8,8+-1,3
# Август: 9,0+0,9
# Сентябрь: 8,9+0,8

# Октябрь: 9,8+-1,2
# Ноябрь: 10,0+-1,6
# Декабрь: 7,4+-1,2


import pandas as pd
import matplotlib.pyplot as plt
from numpy import std, sqrt

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
# coefs.to_excel('rf_coefs.xlsx')
#================================2023========================================#

_2023 = [itogo.loc[i, 'Итого по Столбцам'] for i in itogo.index if '23' in i]
q1 = sum(_2023[:3])
q2 = sum(_2023[3:])
#==================Conclusion: 2023 follows the general trend==================#


q3 = [q2*26.7/24.2, q2*26.7/24.2*sqrt((1.7/24.2)**2+(1.8/26.7)**2)]# 77792 +- 7574
current_jan = _2023[0]
print(current_jan)