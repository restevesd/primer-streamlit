# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:16:21 2022

@author: info
"""
import streamlit as st

st.title('Mi primera página en streamlit')

st.header("Vamos a poner un modelo en producción usando streamlit")

st.subheader("Esto está muy emocionante")

st.text('Esto es un texto de prueba')

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

age = st.slider('How old are you?', 50, 100, 60)
st.write("I'm ", age, 'years old')

st.warning('This is a warning')
st.info("Esto es un info")
st.success('This is a success message!', icon="✅")
