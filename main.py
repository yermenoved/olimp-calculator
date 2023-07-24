import streamlit as st
from math import ceil
import requests
import json

url = 'https://raw.githubusercontent.com/yermenoved/olimp-calculator/main/data.json'
file = requests.get(url)
data = json.loads(file.text)

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



