import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Dashboard Bibliométrico sobre Anemia e Inteligencia Artificial")

# Descripción
st.write("""
Este dashboard muestra investigaciones científicas relacionadas con anemia,
machine learning e inteligencia artificial.
""")

# Leer dataset
df = pd.read_csv("dataset_limpio.csv")

# Mostrar datos
st.subheader("Dataset Científico")
st.dataframe(df)

# Cantidad de artículos
st.subheader("Cantidad de Artículos")
st.write(df.shape[0])

# Conteo por año
articulos_por_anio = df['Year'].value_counts().sort_index()

# Crear gráfico
fig, ax = plt.subplots()

articulos_por_anio.plot(kind='bar', ax=ax)

plt.title('Artículos por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad')

# Mostrar gráfico
st.pyplot(fig)