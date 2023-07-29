import streamlit as st
from math import ceil
import requests
import json

data = {
  "ORTHO Vision":
    {
      "Резус-фактор":
      [
        {
        "707135": 200,
        "6904591": 3060
        },
        [
          [21.3, 2.84],
          [24.2, 1.72],
          [26.7, 1.77],
          [27.2, 2.33]
        ]
      ],

      "Проба Кумбса":
        [
          {
          "707300": 400,
          "100-68": 200,
          "6904591": 3060
          },
          []
        ]
    }
}


# url = 'https://raw.githubusercontent.com/yermenoved/olimp-calculator/main/data.json'
# file = requests.get(url)
# data = json.loads(file.text)

analyzer = st.selectbox(
  'Выберите анализатор:',
  data.keys()
)

test = st.selectbox(
  'Выберите тест:',
  data[analyzer].keys()
)

amount = st.number_input('Введите количество:')

table = data[analyzer][test][0] #load data about this specific test

for element in table.keys():
  st.write('Артикул реагента/расходника:', element, 'Необходимо заявить упаковок:', ceil(amount/table[element]))

print(table, type(table))
