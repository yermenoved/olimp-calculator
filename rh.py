import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('rh.xlsx')

df.index = df['Дата']
df = df.drop(columns='Дата').T
dates = [i.split()[0]+' '+i.split()[1][-2:] for i in df.index]
df.index = dates

itogo = df['Итого по Столбцам'].to_frame()
itogo['SMA'] = itogo['Итого по Столбцам'].rolling(3).mean()

plt.plot(itogo)
plt.xticks(fontsize='xx-small',rotation=90)
plt.show()