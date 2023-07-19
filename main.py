import streamlit as st

analyzers = {
  'ORTHO Vision' : 'Резус-фактор',
}

analyzer = st.selectbox(
  'Выберите анализатор:',
  analyzers.keys()
)

st.write(analyzer)