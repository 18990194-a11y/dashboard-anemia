import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURACIÓN
st.set_page_config(page_title="Dashboard Bibliométrico", layout="wide")

# CARGAR DATASET
df = pd.read_csv("dataset_limpio.csv")

# TÍTULO
st.title("📚 Dashboard Bibliométrico sobre Anemia e Inteligencia Artificial")

st.write("""
Este dashboard analiza investigaciones científicas extraídas desde Scopus
relacionadas con anemia, machine learning e inteligencia artificial.
""")

# MÉTRICAS
st.subheader("📊 Métricas Generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cantidad de artículos", df.shape[0])

with col2:
    st.metric("Total de autores", df['Authors'].nunique())

with col3:
    st.metric("Año más frecuente", df['Year'].mode()[0])

# DATASET
st.subheader("🗂 Dataset Científico")
st.dataframe(df)

# GRÁFICO 1
st.subheader("📈 Publicaciones por Año")

articulos_por_anio = df['Year'].value_counts().sort_index()

fig1, ax1 = plt.subplots()

articulos_por_anio.plot(kind='bar', ax=ax1)

plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.title("Cantidad de publicaciones por año")

st.pyplot(fig1)

# GRÁFICO 2
st.subheader("👨‍🔬 Top 10 Autores")

top_autores = df['Authors'].value_counts().head(10)

fig2, ax2 = plt.subplots()

top_autores.plot(kind='barh', ax=ax2)

plt.xlabel("Cantidad")
plt.ylabel("Autores")
plt.title("Autores con más publicaciones")

st.pyplot(fig2)

# GRÁFICO 3
st.subheader("⭐ Artículos Más Citados")

top_citados = df.sort_values(by='Cited by', ascending=False).head(10)

fig3, ax3 = plt.subplots()

ax3.barh(top_citados['Title'], top_citados['Cited by'])

plt.xlabel("Citas")
plt.ylabel("Artículos")
plt.title("Top artículos más citados")

st.pyplot(fig3)

# CONCLUSIÓN
st.subheader("📝 Conclusión")

st.write("""
La inteligencia artificial y el machine learning están teniendo un crecimiento
importante en investigaciones relacionadas con anemia y salud, observándose un
incremento de publicaciones científicas en los últimos años.
""")