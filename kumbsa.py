import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('kumbsa.xlsx')
df.index = df['Дата']
df = df.drop(columns='Дата').T

itogo = df['Итого по Столбцам'].to_frame()
itogo['SMA'] = itogo['Итого по Столбцам'].rolling(3).mean()

plt.plot(itogo)
plt.xticks(rotation=45)
plt.show()