import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('1.xlsx')

df = df[df.columns[:-2]]

cities = {
    'aktau' : df.loc[2:9],
    'aktobe' : df.loc[10:16],
    'almaty' : df.loc[17:23],
    'astana' : df.loc[24:31],
    'atyrau' : df.loc[32:39],
    'karagandy' : df.loc[40:46],
    'kaskelen' : df.loc[47:53],
    'kokshetau' : df.loc[54:60],
    'kostanay' : df.loc[61:68],
    'kyzylorda': df.loc[69:75],
    'pavlodar' : df.loc[76:82],
    'petropavl' : df.loc[83:89],
    'taldykorgan' : df.loc[90:96],
    'taraz' : df.loc[97:103],
    'turkestan' : df.loc[104:110],
    'oral' : df.loc[111:117],
    'semey' : df.loc[118:125],
    'shymkent': df.loc[126:132]
}

for city in cities:
    cities[city].index = cities[city]['Unnamed: 1']
    cities[city] = cities[city][cities[city].columns[2:]]




