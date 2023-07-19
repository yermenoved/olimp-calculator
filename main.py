import streamlit as st
from math import ceil
import json

data = json.loads('{"ORTHO Vision": {"Резус-фактор": {"707135": 200, "6904591": 3060}, "Проба Кумбса": {"707300": 400, "100-68": 200, "6904591": 3060}}}')

analyzer = st.selectbox(
  'Выберите анализатор:',
  data.keys()
)

test = st.selectbox(
  'Выберите тест:',
  data[analyzer].keys()
)

amount = st.number_input('Введите количество:')

table = data[analyzer][test] #load data about this specific test

for element in table.keys():
  st.write('Артикул реагента/расходника:', element, 'Необходимо заявить упаковок:', ceil(amount/table[element]))
        


