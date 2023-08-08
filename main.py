import streamlit as st
from math import ceil
import requests
import json
from datetime import date

url  = 'https://raw.githubusercontent.com/yermenoved/olimp-calculator/main/data.json'
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

table = data[analyzer][test][0] #load data about this specific test
coefs = data[analyzer][test][1] #season_coefs
current_jan = data[analyzer][test][2]

amount = st.number_input('Введите количество:')

today = date.today()
start = st.date_input('Введите начало интервала:', value=today)
end   = st.date_input('Введите конец интервала:')

for element in table.keys():
  st.write('Артикул:', element, 'Необходимо заявить упаковок:', ceil(amount/table[element]))
