import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv('datos/vehicles_us.csv')

st.header("App de vehiculos")

st.dataframe(datos)

boton = st.checkbox("Visualizar Histograma")

if boton:
    grafico = px.histogram(datos, x='odometer')
    st.plotly_chart(grafico)