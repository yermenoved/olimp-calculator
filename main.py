import streamlit as st
from math import ceil

analyzers = {
  'ORTHO Vision' : ['Резус-фактор', 'Test 2', 'Test 3'],
}

analyzer = st.selectbox(
  'Выберите анализатор:',
  analyzers.keys()
)

test = st.selectbox(
  'Select the test:',
  analyzers[analyzer]
)

amount = st.number_input('Insert the amount:')


        


