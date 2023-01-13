from ast import Import
from turtle import st
import pandas as pd
import streamlit as st
st.write("Primera Aplicacion con Streamlit")
st.write("Podemos escribir lo que queramos, texto, en esta ocasion")

st.write("Incluso un DataFrame como a continuacion")
df = pd.DataFrame({"a": [10, 30, 20, 40, 20], "b": [40, 10, 20, 50, 60]})

st.write(df)
st.write("Podemos plotear un grafico de barras")
st.bar_chart(df)

