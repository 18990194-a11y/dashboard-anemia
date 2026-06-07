import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Dashboard Bibliométrico",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("Navegación")
st.sidebar.write("Proyecto de Ciencia de Datos")
st.sidebar.write("Análisis de investigaciones sobre anemia e inteligencia artificial")

# CARGAR DATASET
df = pd.read_csv("dataset_limpio.csv")

# TÍTULO PRINCIPAL
st.title("Dashboard Bibliométrico sobre Anemia e Inteligencia Artificial")

# MENSAJES
st.success("Bienvenido al dashboard bibliométrico sobre anemia e inteligencia artificial.")

st.info(
    "Los datos fueron obtenidos desde Scopus y analizados utilizando Python, Pandas y Streamlit."
)

# DESCRIPCIÓN
st.write("""
Este dashboard presenta un análisis bibliométrico de artículos científicos
relacionados con anemia, machine learning e inteligencia artificial.
""")

# SEPARADOR
st.markdown("---")

# FILTRO INTERACTIVO
st.subheader("Filtro por Año")

anio = st.selectbox(
    "Seleccione un año",
    sorted(df['Year'].unique())
)

df_filtrado = df[df['Year'] == anio]

# SEPARADOR
st.markdown("---")

# MÉTRICAS
st.subheader("Métricas Generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cantidad de artículos", df.shape[0])

with col2:
    st.metric("Total de autores", df['Authors'].nunique())

with col3:
    st.metric("Año más frecuente", df['Year'].mode()[0])

# SEPARADOR
st.markdown("---")

# DATASET
st.subheader("Dataset Científico Filtrado")

st.dataframe(df_filtrado)

# SEPARADOR
st.markdown("---")

# GRÁFICO 1
st.subheader("Cantidad de Publicaciones por Año")

articulos_por_anio = df['Year'].value_counts().sort_index()

fig1, ax1 = plt.subplots()

articulos_por_anio.plot(
    kind='bar',
    ax=ax1
)

plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.title("Publicaciones por Año")

st.pyplot(fig1)

# SEPARADOR
st.markdown("---")

# GRÁFICO 2
st.subheader("Autores con Más Publicaciones")

top_autores = df['Authors'].value_counts().head(10)

fig2, ax2 = plt.subplots()

top_autores.plot(
    kind='barh',
    ax=ax2
)

plt.xlabel("Cantidad")
plt.ylabel("Autores")
plt.title("Top 10 Autores")

st.pyplot(fig2)

# SEPARADOR
st.markdown("---")

# GRÁFICO 3
st.subheader("Artículos Más Citados")

top_citados = df.sort_values(
    by='Cited by',
    ascending=False
).head(10)

fig3, ax3 = plt.subplots()

ax3.barh(
    top_citados['Title'],
    top_citados['Cited by']
)

plt.xlabel("Cantidad de citas")
plt.ylabel("Artículos")
plt.title("Top Artículos Más Citados")

st.pyplot(fig3)

# SEPARADOR
st.markdown("---")

# CONCLUSIÓN
st.subheader("Conclusión")

st.write("""
La inteligencia artificial y el machine learning han incrementado su presencia
en investigaciones relacionadas con anemia y salud. El análisis bibliométrico
permite identificar tendencias científicas, autores relevantes y artículos
de alto impacto académico.
""")

# PIE DE PÁGINA
st.markdown("---")

st.caption("Proyecto desarrollado con Streamlit, Python y Scopus")