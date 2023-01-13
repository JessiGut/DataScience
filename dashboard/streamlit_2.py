# para ejecutar darle a Run python file, luego streamlit run <nombre del scrip(streamlit_2.py)> 


import streamlit as st

def suma(a, b):
	return a + b
if st.button("suma"):
	resultado = suma(5, 10)
	st.write("el resultado de los numeros es: ", resultado)
    