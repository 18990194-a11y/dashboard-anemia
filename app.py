import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Dashboard Bibliométrico",
    layout="wide"
)


# CARGAR DATASET
df = pd.read_csv("dataset_limpio.csv")

# SIDEBAR
st.sidebar.title("📊 Panel de Control")

st.sidebar.write(
    "Utilice estos filtros para explorar la bibliografía científica."
)

# FILTRO POR PALABRA
busqueda = st.sidebar.text_input(
    "🔍 Buscar palabra clave"
)

# FILTRO POR AÑO
anio = st.sidebar.selectbox(
    "📅 Seleccione un año",
    sorted(df['Year'].unique())
)

# FILTRO POR CITAS
min_citas = st.sidebar.slider(
    "⭐ Mínimo de citas",
    0,
    int(df['Cited by'].max()),
    0
)

# TÍTULO PRINCIPAL
st.title("Dashboard Bibliométrico sobre Anemia e Inteligencia Artificial")


# INTEGRANTE
st.markdown("### 👩‍💻 Integrante")

st.write("""
- Rosa María Flores Echeverría
""")

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
# FILTRAR DATOS

df_filtrado = df[
    (df['Year'] == anio) &
    (df['Cited by'] >= min_citas)
]

if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['Title'].str.contains(
            busqueda,
            case=False,
            na=False
        )
    ]

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

# GRÁFICO CIRCULAR

st.subheader("📚 Distribución de Publicaciones por Año")

tipos = df['Year'].value_counts()

fig4, ax4 = plt.subplots(figsize=(8,8))

ax4.pie(
    tipos,
    ax4.pie(
    tipos,
    autopct=lambda p: f'{p:.1f}%' if p > 5 else '',
    startangle=90
)
ax4.legend(
    tipos.index,
    title="Años",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

# AGUJERO CENTRAL
centro = plt.Circle((0,0), 0.70, fc='white')

fig4.gca().add_artist(centro)

plt.title("Distribución de Publicaciones")

st.pyplot(fig4)

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